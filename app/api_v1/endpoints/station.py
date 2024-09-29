from typing import Annotated
from fastapi import APIRouter, Depends, status

from api_v1.dependencies import station_service
from schemas.station import StationCreate, StationOut, StationRelOut, StationUpdate
from services import StationService


router = APIRouter()


@router.get("/", response_model=list[StationRelOut])
async def get_stations(
    station_service: Annotated[StationService, Depends(station_service)],
) -> list[StationRelOut]:
    return await station_service.get_all_stations()


@router.get("/{station_id}", response_model=StationRelOut)
async def get_station(
    station_id: int,
    station_service: Annotated[StationService, Depends(station_service)],
) -> StationRelOut:
    return await station_service.get_station_by_id(station_id=station_id)


@router.post("/", response_model=StationOut, status_code=status.HTTP_201_CREATED)
async def create_station(
    station_in: StationCreate,
    station_service: Annotated[StationService, Depends(station_service)],
) -> StationOut:
    return await station_service.create_station(station_in=station_in)


@router.put("/{station_id}", response_model=StationOut)
async def update_station(
    station_id: int,
    station_update: StationUpdate,
    station_service: Annotated[StationService, Depends(station_service)],
) -> StationOut:
    return await station_service.update_station(
        station_id=station_id,
        station_update=station_update,
    )


@router.delete(
    "/{station_id}", response_model=None, status_code=status.HTTP_204_NO_CONTENT
)
async def delete_station(
    station_id: int,
    station_service: Annotated[StationService, Depends(station_service)],
) -> None:
    await station_service.delete_station(station_id=station_id)
