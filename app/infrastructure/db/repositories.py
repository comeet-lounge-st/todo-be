import uuid

from app.infrastructure.db.models import User
from config.settings import settings
from fastapi_users import BaseUserManager, UUIDIDMixin


class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    verification_token_secret = settings.access_token_secret
    reset_password_token_secret = settings.reset_password_token_secret
