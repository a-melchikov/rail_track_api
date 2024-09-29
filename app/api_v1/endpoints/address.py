from typing import Annotated
from fastapi import APIRouter, Depends, status

from schemas.address import AddressOut, AddressCreate, AddressUpdate
from services.address import AddressService
from api_v1.dependencies import address_service

router = APIRouter()


@router.get("/", response_model=list[AddressOut])
async def get_addresses(
    address_service: Annotated[AddressService, Depends(address_service)],
) -> list[AddressOut]:
    return await address_service.get_all_addresses()


@router.get("/{address_id}", response_model=AddressOut)
async def get_address(
    address_id: int,
    address_service: Annotated[AddressService, Depends(address_service)],
) -> AddressOut:
    return await address_service.get_address_by_id(address_id=address_id)


@router.post("/", response_model=AddressOut, status_code=status.HTTP_201_CREATED)
async def create_address(
    address_in: AddressCreate,
    address_service: Annotated[AddressService, Depends(address_service)],
) -> AddressOut:
    return await address_service.create_address(address_in=address_in)


@router.put("/{address_id}", response_model=AddressOut)
async def update_address(
    address_id: int,
    address_update: AddressUpdate,
    address_service: Annotated[AddressService, Depends(address_service)],
) -> AddressOut:
    return await address_service.update_address(
        address_id=address_id,
        address_update=address_update,
    )


@router.delete(
    "/{address_id}", response_model=None, status_code=status.HTTP_204_NO_CONTENT
)
async def delete_address(
    address_id: int,
    address_service: Annotated[AddressService, Depends(address_service)],
) -> None:
    await address_service.delete_address(address_id=address_id)
