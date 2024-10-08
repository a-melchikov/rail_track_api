from __future__ import annotations
from typing import TYPE_CHECKING

from sqlalchemy import String, CHAR, ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import Base
from db.mixins import IdMixin


if TYPE_CHECKING:
    from db import Address, Train, Personnel, Route, RouteDetail


class Station(IdMixin, Base):
    __table_args__ = (
        CheckConstraint(
            "length(tax_id)=12",
            name="check_tax_id_length",
        ),
    )

    name: Mapped[str] = mapped_column(String(255))
    tax_id: Mapped[str] = mapped_column(CHAR(12), unique=True)
    address_id: Mapped[int] = mapped_column(
        ForeignKey("addresses.id", ondelete="CASCADE"),
        unique=True,
    )

    address: Mapped[Address] = relationship(
        back_populates="stations",
    )
    trains: Mapped[list[Train]] = relationship(
        secondary="train_station_association",
        back_populates="stations",
    )
    personnel: Mapped[list[Personnel]] = relationship(back_populates="station")

    owned_routes: Mapped[list[Route]] = relationship(
        foreign_keys="[Route.owner_station_id]",
        back_populates="owner_station",
    )
    departure_routes: Mapped[list[Route]] = relationship(
        foreign_keys="[Route.departure_station_id]",
        back_populates="departure_station",
    )
    arrival_routes: Mapped[list[Route]] = relationship(
        foreign_keys="[Route.arrival_station_id]",
        back_populates="arrival_station",
    )
    stop_details: Mapped[list[RouteDetail]] = relationship(
        back_populates="stop_station"
    )

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id}, name={self.name}, tax_id={self.tax_id}, address_id={self.address_id})"

    def __repr__(self) -> str:
        return str(self)
