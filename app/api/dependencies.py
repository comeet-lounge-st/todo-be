from app.infrastructure.db.session import SessionLocal
from sqlalchemy.ext.asyncio import AsyncSession


def get_db() -> AsyncSession:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
