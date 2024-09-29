from db.repositories import AddressRepository, StationRepository
from services import AddressService, StationService


async def address_service():
    return AddressService(AddressRepository)


async def station_service():
    return StationService(StationRepository)
