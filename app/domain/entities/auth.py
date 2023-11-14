import uuid

from config.settings import settings
from fastapi_users import schemas
from pydantic import BaseModel


class SigninRequest(BaseModel):
    email: str
    password: str


class SignupRequest(BaseModel):
    email: str
    password: str
    name: str


class RefreshTokenRequest(BaseModel):
    refreshToken: str


class SigninResponse(BaseModel):
    token: str
    refreshToken: str


class SignupResponse(BaseModel):
    id: uuid.UUID


class UserReadResponse(BaseModel):
    id: uuid.UUID
    email: str
    name: str


class UserRead(schemas.BaseUser[uuid.UUID]):
    name: str


class UserCreate(schemas.BaseUserCreate):
    name: str


class UserUpdate(schemas.BaseUserUpdate):
    pass
