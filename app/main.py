from fastapi import FastAPI

from api_v1 import router as router_v1
from core import settings

app = FastAPI()
app.include_router(router=router_v1, prefix=settings.api_v1_prefix)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True)
