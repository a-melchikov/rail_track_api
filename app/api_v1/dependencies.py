from db.repositories import AddressRepository
from services.address import AddressService


async def address_service():
    return AddressService(AddressRepository)
