from app.api.dependencies import get_current_user
from app.domain.entities.auth import UserReadResponse
from app.domain.entities.common import ErrorResponse
from app.infrastructure.db.models import User
from fastapi import APIRouter, Depends, Request, status

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.get(
    "/me",
    name="users:me",
    response_model=UserReadResponse,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {
            "description": "유저 정보 조회 성공",
        },
        status.HTTP_401_UNAUTHORIZED: {
            "description": "인증 실패",
            "model": ErrorResponse,
        },
    },
)
async def me(
    request: Request,
    current_user: User = Depends(get_current_user),
) -> UserReadResponse:
    return UserReadResponse.from_orm(current_user)
