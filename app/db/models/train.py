from __future__ import annotations
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import Base
from db.mixins import IdMixin

if TYPE_CHECKING:
    from db import Station, TrainType, Route


class Train(IdMixin, Base):
    name: Mapped[str] = mapped_column(String(255), unique=True)
    train_type_id: Mapped[int] = mapped_column(ForeignKey("train_types.id"))

    stations: Mapped[list[Station]] = relationship(
        secondary="train_station_association",
        back_populates="trains",
    )
    train_type: Mapped[TrainType] = relationship(back_populates="trains")
    routes: Mapped[list[Route]] = relationship(back_populates="train")

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id}, name={self.name}, station_id={self.station_id}, train_type_id={self.train_type_id}"

    def __repr__(self) -> str:
        return str(self)
