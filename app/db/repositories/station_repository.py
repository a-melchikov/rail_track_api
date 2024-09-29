import asyncio

from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from db import db_helper, Station
from schemas import station
from schemas.station import StationOut, StationRelOut
from utils.repository import SQLAlchemyRepository


class StationRepository(SQLAlchemyRepository):
    model: Station = Station
    schema: StationOut = StationOut
    schema_rel: StationRelOut = StationRelOut

    async def find_one(self, id: int) -> StationRelOut:
        async with db_helper.session_factory() as session:
            stmt = (
                select(self.model)
                .where(self.model.id == id)
                .options(selectinload(self.model.address))
            )
            result = await session.execute(stmt)
            station = result.scalar_one_or_none()
            if not station:
                raise ValueError(f"Station with id {id} not found")
            return self.schema_rel.model_validate(station)

    async def find_all(self) -> list[BaseModel]:
        async with db_helper.session_factory() as session:
            stmt = select(self.model).options(selectinload(self.model.address)).order_by(self.model.id)
            result = await session.execute(stmt)
            stations = result.scalars().all()
            return [
                self.schema_rel.model_validate(station, from_attributes=True)
                for station in stations
            ]

    async def find_one_by_field(self, field: str, value) -> StationOut | None:
        async with db_helper.session_factory() as session:
            stmt = select(self.model).where(getattr(self.model, field) == value)
            result = await session.execute(stmt)
            station = result.scalar_one_or_none()
            if station:
                return self.schema.model_validate(station)
            return None


async def main():
    async with db_helper.session_factory() as session:
        pass


if __name__ == "__main__":
    asyncio.run(main())
