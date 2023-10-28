import uuid

from config.settings import settings
from fastapi_users import schemas
from pydantic import BaseModel


class SigninResponse(BaseModel):
    token: str
    refreshToken: str
    tokenType: str = "bearer"
    expires: int = settings.access_token_expiration


class UserRead(schemas.BaseUser[uuid.UUID]):
    pass


class UserCreate(schemas.BaseUserCreate):
    pass


class UserUpdate(schemas.BaseUserUpdate):
    pass
