from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from schemas.address import AddressOut, AddressCreate, AddressUpdate
from utils.repository import AbstractRepository


class AddressService:
    def __init__(self, address_repo: AbstractRepository):
        self.address_repo: AbstractRepository = address_repo()

    async def create_address(
        self,
        address_in: AddressCreate,
    ) -> AddressOut:
        try:
            address_dict = address_in.model_dump()
            address = await self.address_repo.add_one(address_dict)
            return AddressOut(**address)
        except SQLAlchemyError as e:
            raise RuntimeError("Failed to create address") from e

    async def get_all_addresses(
        self,
    ) -> list[AddressOut]:
        try:
            addresses = await self.address_repo.find_all()
            return [AddressOut(**address) for address in addresses]
        except SQLAlchemyError as e:
            raise RuntimeError("Failed to retrieve addresses") from e

    async def get_address_by_id(
        self,
        address_id: int,
    ) -> AddressOut:
        try:
            address = await self.address_repo.find_one(id=address_id)
            return AddressOut(**address)
        except ValueError:
            raise HTTPException(
                status_code=404, detail=f"Address with id {address_id} not found"
            )
        except SQLAlchemyError as e:
            raise RuntimeError("Failed to retrieve address") from e

    async def update_address(
        self,
        address_id: int,
        address_update: AddressUpdate,
    ) -> AddressOut:
        try:
            address_dict = address_update.model_dump(exclude_unset=True)
            address = await self.address_repo.update_one(address_id, address_dict)
            return AddressOut(**address)
        except ValueError:
            raise HTTPException(
                status_code=404, detail=f"Address with id {address_id} not found"
            )
        except SQLAlchemyError as e:
            raise RuntimeError(f"Failed to update address {id}") from e

    async def delete_address(
        self,
        address_id: int,
    ) -> None:
        try:
            await self.address_repo.delete_one(address_id)
        except ValueError:
            raise HTTPException(
                status_code=404, detail=f"Address with id {address_id} not found"
            )
        except SQLAlchemyError as e:
            raise RuntimeError(f"Failed to delete address {address_id}") from e
