from __future__ import annotations
from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import Base
from db.mixins import IdMixin

if TYPE_CHECKING:
    from db import Train


class TrainType(IdMixin, Base):
    __tablename__ = "train_types"

    type_name: Mapped[str] = mapped_column(String(100), unique=True)

    trains: Mapped[list[Train]] = relationship(back_populates="train_type")

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id}, type_name={self.type_name}"

    def __repr__(self) -> str:
        return str(self)
