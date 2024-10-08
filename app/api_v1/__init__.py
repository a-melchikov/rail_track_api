from fastapi import APIRouter


from .endpoints.address import router as addresses_router
from .endpoints.station import router as stations_router
from .endpoints.train_type import router as train_type_router
from .endpoints.train import router as train_router

router = APIRouter()
router.include_router(router=addresses_router, prefix="/addresses", tags=["Address"])
router.include_router(router=stations_router, prefix="/stations", tags=["Station"])
router.include_router(
    router=train_type_router, prefix="/train_type", tags=["Train Type"]
)
router.include_router(router=train_router, prefix="/train", tags=["Train"])
