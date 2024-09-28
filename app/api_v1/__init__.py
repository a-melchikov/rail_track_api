from fastapi import APIRouter


from .endpoints.address import router as addresses_router
from .endpoints.station import router as stations_router

router = APIRouter()
router.include_router(router=addresses_router, prefix="/addresses", tags=["Address"])
router.include_router(router=stations_router, prefix="/stations", tags=["Station"])
