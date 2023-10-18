from functools import lru_cache

from fastapi import Depends, FastAPI
from typing_extensions import Annotated
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Awesome API"
    admin_email: str
    items_per_user: int = 50

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')


app = FastAPI()


@lru_cache(maxsize=1)
def get_settings():
    return Settings()


@app.get("/info")
async def info(settings: Annotated[Settings, Depends(get_settings)]):
    return {
        "app_name": settings.app_name,
        "admin_email": settings.admin_email,
        "items_per_user": settings.items_per_user,
    }
