import uuid
from typing import Annotated

from app.api.dependencies import get_user_manager
from app.domain.entities.auth import (
    SigninRequest,
    SigninResponse,
    SignupRequest,
    SignupResponse,
    UserCreate,
    UserRead,
)
from app.infrastructure.db.models import User
from app.infrastructure.services.jwt import access_token_backend, refresh_token_backend
from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_users import BaseUserManager, FastAPIUsers, exceptions, models, schemas
from fastapi_users.authentication.strategy.base import Strategy

router = APIRouter(
    tags=["auth"],
)

fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [access_token_backend, refresh_token_backend],
)


@router.post(
    "/sign-in",
    name="auth:sign-in",
    response_model=SigninResponse,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {
            "description": "로그인 성공",
        },
        status.HTTP_400_BAD_REQUEST: {
            "description": "로그인 실패",
        },
    },
)
async def sign_in(
    request: Request,
    credentials: Annotated[SigninRequest, Depends()],
    user_manager: Annotated[
        BaseUserManager[models.UP, models.ID], Depends(get_user_manager)
    ],
    access_token_strategy: Annotated[
        Strategy[models.UP, models.ID], Depends(access_token_backend.get_strategy)
    ],
    refresh_token_strategy: Annotated[
        Strategy[models.UP, models.ID], Depends(refresh_token_backend.get_strategy)
    ],
):
    credentials = OAuth2PasswordRequestForm(
        username=credentials.email,
        password=credentials.password,
    )

    user = await user_manager.authenticate(credentials)

    if user is None or not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="주어진 이메일과 비밀번호로 로그인할 수 없습니다.",
        )

    access_token = await access_token_strategy.write_token(user)
    refresh_token = await refresh_token_strategy.write_token(user)

    return SigninResponse(
        token=access_token,
        refreshToken=refresh_token,
    )


@router.post(
    "/sign-up",
    name="auth:sign-up",
    response_model=SignupResponse,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_201_CREATED: {
            "description": "회원가입 성공",
        },
        status.HTTP_400_BAD_REQUEST: {
            "description": "회원가입 실패",
        },
    },
)
async def sign_up(
    request: Request,
    user_create: Annotated[SignupRequest, Depends()],
    user_manager: Annotated[
        BaseUserManager[models.UP, models.ID], Depends(get_user_manager)
    ],
):
    try:
        user_create = UserCreate(
            email=user_create.email,
            password=user_create.password,
            name=user_create.name,
        )
        created_user = await user_manager.create(
            user_create, safe=True, request=request
        )
    except exceptions.UserAlreadyExists:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="이미 존재하는 이메일입니다.",
        )
    except exceptions.InvalidPasswordException as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e.reason,
        )

    user = schemas.model_validate(UserRead, created_user)
    return SignupResponse(id=user.id)
