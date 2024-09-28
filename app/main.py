from contextlib import asynccontextmanager
import uvicorn

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from api_v1 import router as router_v1
from core import settings
from db import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await db_helper.dispose()


main_app = FastAPI(
    default_response_class=ORJSONResponse,
    lifespan=lifespan,
)
main_app.include_router(router=router_v1, prefix=settings.api_v1_prefix)

if __name__ == "__main__":
    uvicorn.run("main:main_app", reload=True)
