from typing import Annotated
from fastapi import Depends

from db.repositories import (
    AddressRepository,
    StationRepository,
    TrainTypeRepository,
    TrainRepository,
)
from services import (
    AddressService,
    StationService,
    TrainTypeService,
    TrainService,
)


async def address_service():
    return AddressService(AddressRepository)


async def station_service():
    return StationService(StationRepository)


async def train_type_service():
    return TrainTypeService(TrainTypeRepository)


async def train_service():
    return TrainService(TrainRepository)


train_type_service_dependency = Annotated[TrainTypeService, Depends(train_type_service)]
train_service_dependency = Annotated[TrainService, Depends(train_service)]
