from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Awesome API"
    admin_email: str
    database_url: str
    items_per_user: int = 50
    access_token_secret: str
    access_token_expiration: int = 60 * 60 * 1  # 1 hour
    refresh_token_secret: str
    refresh_token_expiration: int = 60 * 60 * 24 * 7  # 7 days
    reset_password_token_secret: str

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
