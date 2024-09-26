from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from db import db_helper, AddressRepository
from schemas.address import Address, AddressCreate

router = APIRouter(tags=["Address"])


@router.post("/", response_model=Address, status_code=status.HTTP_201_CREATED)
async def create_address(
    address_in: AddressCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    address_repo = AddressRepository(session=session)
    return await address_repo.create_address(address_in=address_in)
