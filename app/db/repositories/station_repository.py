import asyncio

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db import Station, db_helper
from schemas.station import StationCreate, StationUpdate


class StationRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_station(
        self,
        station_in: StationCreate,
    ) -> Station:
        station = Station(**station_in.model_dump())
        self.session.add(station)
        try:
            await self.session.commit()
        except Exception as e:
            await self.session.rollback()
            raise e
        return station

    async def get_station_by_id(
        self,
        station_id: int,
    ) -> Station | None:
        return await self.session.get(Station, station_id)

    async def get_all_stations(
        self,
    ) -> list[Station]:
        stmt = select(Station).order_by(Station.id)
        stations = await self.session.scalars(stmt)
        return list(stations)

    async def update_station(
        self, station: Station, station_update: StationUpdate
    ) -> Station:
        for name, value in station_update.model_dump(exclude_unset=True).items():
            setattr(station, name, value)
        try:
            await self.session.commit()
        except Exception as e:
            await self.session.rollback()
            raise e
        return station

    async def delete_station(
        self,
        station: Station,
    ) -> None:
        await self.session.delete(station)
        try:
            await self.session.commit()
        except Exception as e:
            await self.session.rollback()
            raise e


async def main():
    async with db_helper.session_factory() as session:
        pass


if __name__ == "__main__":
    asyncio.run(main())
