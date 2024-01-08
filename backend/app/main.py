from contextlib import asynccontextmanager

from beanie import init_beanie
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

from .config import settings
from .models import URL
from .routers import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.client = AsyncIOMotorClient(
        settings.MONGO_HOST.get_secret_value(),
        int(settings.MONGO_PORT.get_secret_value()),
        username=settings.MONGO_USER.get_secret_value(),
        password=settings.MONGO_PASSWORD.get_secret_value(),
    )
    await init_beanie(database=app.client[settings.MONGO_DB.get_secret_value()], document_models=[URL])

    yield


app = FastAPI(
    title=settings.PROJECT_NAME,
    lifespan=lifespan,
)

app.include_router(router)


@app.get("/")
async def root():
    return {"message": "Short-URL ROOT"}
