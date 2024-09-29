from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from db import db_helper
from db.repositories import StationRepository
from schemas.station import StationOut, StationCreate, StationUpdate
from dependencies.station import station_by_id

router = APIRouter()


@router.get("/", response_model=list[StationOut])
async def get_stations(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> list[StationOut]:
    station_repo = StationRepository(session=session)
    return await station_repo.get_all_stations()


@router.get("/{station_id}/", response_model=StationOut)
async def get_station(
    station: StationOut = Depends(station_by_id),
) -> StationOut:
    return station


@router.post("/", response_model=StationOut, status_code=status.HTTP_201_CREATED)
async def create_station(
    station_in: StationCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> StationOut:
    station_repo = StationRepository(session)
    try:
        new_station = await station_repo.create_station(station_in)
    except IntegrityError:
        await session.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="StationOut already exists."
        )
    return new_station


@router.put("/{station_id}/", response_model=StationOut)
async def update_station(
    station_update: StationUpdate,
    station: StationOut = Depends(station_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> StationOut:
    station_repo = StationRepository(session=session)
    return await station_repo.update_Station(
        station=station,
        station_update=station_update,
    )


@router.delete(
    "/{station_id}/", response_model=None, status_code=status.HTTP_204_NO_CONTENT
)
async def delete_station(
    station: StationOut = Depends(station_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    station_repo = StationRepository(session=session)
    return await station_repo.delete_station(
        station=station,
    )
