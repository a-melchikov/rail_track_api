from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from db import db_helper, AddressRepository
from db import Address
from schemas.address import AddressOut, AddressCreate, AddressUpdate
from dependencies.address import address_by_id

router = APIRouter(tags=["Address"])


@router.get("/", response_model=list[AddressOut])
async def get_addresses(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> list[Address]:
    address_repo = AddressRepository(session=session)
    return await address_repo.get_all_addresses()


@router.get("/{address_id}/", response_model=AddressOut)
async def get_address(
    address: Address = Depends(address_by_id),
):
    return address


@router.post("/", response_model=AddressOut, status_code=status.HTTP_201_CREATED)
async def create_address(
    address_in: AddressCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    address_repo = AddressRepository(session=session)
    return await address_repo.create_address(address_in=address_in)


@router.put("/{address_id}/", response_model=AddressOut)
async def update_address(
    address_update: AddressUpdate,
    address: Address = Depends(address_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    address_repo = AddressRepository(session=session)
    return await address_repo.update_address(
        address=address,
        address_update=address_update,
    )


@router.delete(
    "/{address_id}/", response_model=None, status_code=status.HTTP_204_NO_CONTENT
)
async def delete_address(
    address: Address = Depends(address_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    address_repo = AddressRepository(session=session)
    return await address_repo.delete_address(
        address=address,
    )
