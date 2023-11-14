from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from sqlalchemy import Column, String

from .session import Base


class User(SQLAlchemyBaseUserTableUUID, Base):
    name = Column(String(32), nullable=False)
