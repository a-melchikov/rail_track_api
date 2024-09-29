from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError

from db.repositories.station_repository import StationRepository
from schemas.station import StationOut, StationCreate, StationUpdate, StationRelOut
from utils.repository import AbstractRepository


class StationService:
    def __init__(self, station_repo: AbstractRepository):
        self.station_repo: StationRepository = station_repo()

    async def get_all_stations(
        self,
    ) -> list[StationRelOut]:
        try:
            stations = await self.station_repo.find_all()
            return stations
        except SQLAlchemyError as e:
            raise RuntimeError("Failed to retrieve stations") from e

    async def get_station_by_id(
        self,
        station_id: int,
    ) -> StationRelOut:
        try:
            station = await self.station_repo.find_one(id=station_id)
            return station
        except ValueError:
            raise HTTPException(
                status_code=404, detail=f"Station with id {station_id} not found"
            )
        except SQLAlchemyError as e:
            raise RuntimeError("Failed to retrieve station") from e

    async def create_station(self, station_in: StationCreate) -> StationOut:
        existing_station = await self.station_repo.find_one_by_field(
            "address_id", station_in.address_id
        )
        if existing_station:
            raise HTTPException(
                status_code=400,
                detail=f"Address with id {station_in.address_id} is already associated with another station",
            )
        try:
            station = await self.station_repo.add_one(station_in)
            return station
        except SQLAlchemyError as e:
            raise RuntimeError("Failed to create station") from e

    async def update_station(
        self, station_id: int, station_update: StationUpdate
    ) -> StationOut:
        if station_update.address_id is not None:
            existing_station = await self.station_repo.find_one_by_field(
                "address_id", station_update.address_id
            )
            if existing_station and existing_station.id != station_id:
                raise HTTPException(
                    status_code=400,
                    detail=f"Address with id {station_update.address_id} is already associated with another station",
                )
        try:
            station = await self.station_repo.update_one(station_id, station_update)
            return station
        except SQLAlchemyError as e:
            raise RuntimeError(f"Failed to update station {station_id}") from e

    async def delete_station(self, station_id: int) -> None:
        try:
            await self.station_repo.delete_one(station_id)
        except ValueError:
            raise HTTPException(
                status_code=404, detail=f"Station with id {station_id} not found"
            )
        except SQLAlchemyError as e:
            raise RuntimeError(f"Failed to delete station {station_id}") from e
