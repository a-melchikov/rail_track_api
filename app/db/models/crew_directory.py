from __future__ import annotations
from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import Base
from db.mixins import IdMixin

if TYPE_CHECKING:
    from db import Personnel


class CrewDirectory(IdMixin, Base):
    __tablename__ = "crew_directories"

    crew_name: Mapped[str] = mapped_column(String(255), unique=True)

    personnel: Mapped[list[Personnel]] = relationship(back_populates="crew")

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id}, crew_name={self.crew_name})"

    def __repr__(self) -> str:
        return str(self)
