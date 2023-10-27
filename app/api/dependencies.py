from typing import AsyncGenerator

from app.infrastructure.db.session import async_session_maker
from sqlalchemy.ext.asyncio import AsyncSession


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
