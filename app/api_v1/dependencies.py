from db.repositories import AddressRepository, StationRepository, TrainTypeRepository
from services import AddressService, StationService, TrainTypeService


async def address_service():
    return AddressService(AddressRepository)


async def station_service():
    return StationService(StationRepository)


async def train_type_service():
    return TrainTypeService(TrainTypeRepository)
