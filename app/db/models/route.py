from __future__ import annotations
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import Base
from db.mixins import IdMixin

if TYPE_CHECKING:
    from db import Station, Train, CrewDirectory, RouteDetail


class Route(IdMixin, Base):
    train_id: Mapped[int] = mapped_column(ForeignKey("trains.id"))
    crew_id: Mapped[int] = mapped_column(ForeignKey("crew_directories.id"))
    owner_station_id: Mapped[int] = mapped_column(ForeignKey("stations.id"))
    departure_station_id: Mapped[int] = mapped_column(ForeignKey("stations.id"))
    arrival_station_id: Mapped[int] = mapped_column(ForeignKey("stations.id"))
    departure_time: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP)
    arrival_time: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP)

    owner_station: Mapped[Station] = relationship(
        foreign_keys=[owner_station_id],
        back_populates="owned_routes",
    )
    departure_station: Mapped[Station] = relationship(
        foreign_keys=[departure_station_id],
        back_populates="departure_routes",
    )
    arrival_station: Mapped[Station] = relationship(
        foreign_keys=[arrival_station_id],
        back_populates="arrival_routes",
    )
    train: Mapped[Train] = relationship(back_populates="routes")
    crew: Mapped[CrewDirectory] = relationship(back_populates="routes")
    route_details: Mapped[list[RouteDetail]] = relationship(back_populates="route")

    def __str__(self) -> str:
        return (
            f"Route(id={self.id}, owner_station_id={self.owner_station_id}, "
            f"train_id={self.train_id}, departure_station_id={self.departure_station_id}, "
            f"arrival_station_id={self.arrival_station_id}, crew_id={self.crew_id},departure_time={self.departure_time}, "
            f"arrival_time={self.arrival_time})"
        )

    def __repr__(self) -> str:
        return str(self)
