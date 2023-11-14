from functools import lru_cache

from config.settings import Settings, settings
from fastapi import Depends, FastAPI
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing_extensions import Annotated

from app.api.routes import auth, task, users

app = FastAPI(
    title=settings.app_name,
)

app.include_router(task.router)
app.include_router(auth.router)
app.include_router(users.router)


@lru_cache(maxsize=1)
def get_settings():
    return settings


@app.get("/info")
async def info(settings: Annotated[Settings, Depends(get_settings)]):
    return {
        "app_name": settings.app_name,
        "admin_email": settings.admin_email,
        "items_per_user": settings.items_per_user,
    }
