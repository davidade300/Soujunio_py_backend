from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from sou_junior.core.db import DBHandler, SessionLocal, engine

db_handler: DBHandler = DBHandler(engine, SessionLocal)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async for session in db_handler.get_session():
        yield session
