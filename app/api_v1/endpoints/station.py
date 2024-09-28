from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from db import db_helper
from db.repositories import StationRepository
from schemas.station import Station, StationCreate, StationUpdate
from dependencies.station import station_by_id

router = APIRouter()


@router.get("/", response_model=list[Station])
async def get_stations(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> list[Station]:
    station_repo = StationRepository(session=session)
    return await station_repo.get_all_stations()


@router.get("/{station_id}/", response_model=Station)
async def get_station(
    station: Station = Depends(station_by_id),
) -> Station:
    return station


@router.post("/", response_model=Station, status_code=status.HTTP_201_CREATED)
async def create_station(
    station_in: StationCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Station:
    station_repo = StationRepository(session=session)
    return await station_repo.create_station(station_in == station_in)


@router.put("/{station_id}/", response_model=Station)
async def update_station(
    station_update: StationUpdate,
    station: Station = Depends(station_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Station:
    station_repo = StationRepository(session=session)
    return await station_repo.update_Station(
        station=station,
        station_update=station_update,
    )


@router.delete(
    "/{station_id}/", response_model=None, status_code=status.HTTP_204_NO_CONTENT
)
async def delete_station(
    station: Station = Depends(station_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    station_repo = StationRepository(session=session)
    return await station_repo.delete_station(
        station=station,
    )
