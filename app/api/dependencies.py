import uuid
from typing import AsyncGenerator

from app.infrastructure.db.models import User
from app.infrastructure.db.repositories import UserManager
from app.infrastructure.db.session import async_session_maker
from app.infrastructure.services.jwt import access_token_backend, refresh_token_backend
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from fastapi_users import FastAPIUsers
from fastapi_users.db import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)


async def get_user_manager(user_db=Depends(get_user_db)):
    return UserManager(user_db)


fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [access_token_backend],
)

current_active_user = fastapi_users.current_user(active=True)


async def get_current_user(
    token: str = Depends(HTTPBearer(auto_error=True)),
    access_token_strategy=Depends(access_token_backend.get_strategy),
    user_manager=Depends(get_user_manager),
) -> User:
    user = await access_token_strategy.read_token(token.credentials, user_manager)
    if not user:
        raise HTTPException(status_code=401, detail="Not authenticated")
    return user
