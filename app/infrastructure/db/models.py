from fastapi_users.db import SQLAlchemyBaseUserTableUUID

from .session import Base


class User(SQLAlchemyBaseUserTableUUID, Base):
    pass
