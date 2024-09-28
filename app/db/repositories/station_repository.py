from sqlalchemy.ext.asyncio import AsyncSession
from db import Station


class StationRepository:
    def __init__(
        self,
        session: AsyncSession,
    ):
        self.session = session

    def create_station() -> Station:
        pass
