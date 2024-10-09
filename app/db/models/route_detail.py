from __future__ import annotations
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import Base

if TYPE_CHECKING:
    from db import Route, Station


class RouteDetail(Base):
    __tablename__ = "route_details"

    stop_number: Mapped[int] = mapped_column(primary_key=True)
    route_id: Mapped[int] = mapped_column(
        ForeignKey("routes.id", ondelete="CASCADE"), primary_key=True
    )
    stop_station_id: Mapped[int] = mapped_column(ForeignKey("stations.id"))
    arrival_time: Mapped[TIMESTAMP | None] = mapped_column(TIMESTAMP)
    departure_time: Mapped[TIMESTAMP | None] = mapped_column(TIMESTAMP)

    route: Mapped[Route] = relationship(back_populates="route_details")
    stop_station: Mapped[Station] = relationship(back_populates="stop_details")

    def __str__(self) -> str:
        return f"RouteDetail(route_id={self.route_id}, stop_number={self.stop_number}, stop_station_id={self.stop_station_id})"

    def __repr__(self) -> str:
        return str(self)
