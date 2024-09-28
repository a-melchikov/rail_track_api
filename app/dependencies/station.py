from typing import Annotated

from fastapi import Depends, HTTPException, Path, status
from sqlalchemy.ext.asyncio import AsyncSession

from db import Station, db_helper
from db.repositories import StationRepository


async def station_by_id(
    station_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Station:
    station_repo = StationRepository(session=session)
    station = await station_repo.get_station_by_id(station_id=station_id)
    if station:
        return station
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Station {station_id} not found!"
    )
