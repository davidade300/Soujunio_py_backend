from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from sou_junior.core.settings import settings

engine: AsyncEngine = create_async_engine(
    url=settings.DATABASE_URL,
    echo=True,
)

SessionLocal = async_sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    class_=AsyncSession,
)


class DBHandler:
    def __init__(
        self, db_engine: AsyncEngine, session_factory: async_sessionmaker[AsyncSession]
    ) -> None:
        self.engine: AsyncEngine = db_engine
        self.session_factory: async_sessionmaker[AsyncSession] = session_factory

    async def get_session(self) -> AsyncGenerator[AsyncSession]:
        async with self.session_factory() as db:
            try:
                yield db
                await db.commit()
            except Exception:
                await db.rollback()
                raise
