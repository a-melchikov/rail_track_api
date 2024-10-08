from __future__ import annotations
from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import Base
from db.mixins import IdMixin

if TYPE_CHECKING:
    from db import Personnel


class Position(IdMixin, Base):
    position_name: Mapped[str] = mapped_column(String(100), unique=True)

    personnel: Mapped[list[Personnel]] = relationship(back_populates="position")

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id}, position_name={self.position_name})"

    def __repr__(self) -> str:
        return str(self)
