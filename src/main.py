# main.py
from contextlib import asynccontextmanager

from fastapi import FastAPI

from sou_junior.api.v1.workblock import router
from sou_junior.core.db import engine
from sou_junior.models.models import Base


@asynccontextmanager
async def lifespan(_: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)  # type: ignore
    yield


app: FastAPI = FastAPI(title="Log de Performance", lifespan=lifespan)

app.include_router(router)
