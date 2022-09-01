from typing import AsyncGenerator

from app.db.session import SessionLocal


async def get_session() -> AsyncGenerator:
    try:
        session = SessionLocal()
        yield session
    finally:
        await session.close()
