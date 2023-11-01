from fastapi import APIRouter, Request, status

router = APIRouter(
    tags=["task"],
)

@router.get(
    "/tasks/find/{id}",
    name="task:read_one",
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {
            "description": "할일 단건 조회 성공",
        },
        status.HTTP_400_BAD_REQUEST: {
            "description": "할일 단건 조회 실패",
        },
    },
)
async def read_one_task(id):
    pass

@router.get(
    "/tasks/all",
    name="task:read_all",
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {
            "description": "할일 다중건 조회 성공",
        },
        status.HTTP_400_BAD_REQUEST: {
            "description": "할일 다중건 조회 실패",
        },
    },
)
async def read_all_task():
    pass

@router.post(
    "/tasks/create",
    name="task:create",
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {
            "description": "할일 생성 성공",
        },
        status.HTTP_400_BAD_REQUEST: {
            "description": "할일 생성 실패",
        },
    },
)
async def create_task(request: Request):
    pass

@router.put(
    "/tasks/update/{id}",
    name="task:update",
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {
            "description": "할일 수정 성공",
        },
        status.HTTP_400_BAD_REQUEST: {
            "description": "할일 수정 실패",
        },
    },
)
async def update_task(id, request: Request):
    pass

@router.delete(
    "/tasks/delete/{id}",
    name="task:delete",
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {
            "description": "할일 삭제 성공",
        },
        status.HTTP_400_BAD_REQUEST: {
            "description": "할일 삭제 실패",
        },
    },
)
async def delete_task(id):
    pass
