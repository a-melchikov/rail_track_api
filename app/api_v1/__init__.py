from fastapi import APIRouter


from .endpoints.address import router as addresses_router

router = APIRouter()
router.include_router(router=addresses_router, prefix="/addresses")
