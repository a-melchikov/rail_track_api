from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from db import Base
from db.mixins import IdMixin


class CrewDirectory(IdMixin, Base):
    __tablename__ = "crew_directories"

    crew_name: Mapped[str] = mapped_column(String(255), unique=True)

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id}, crew_name={self.crew_name})"

    def __repr__(self) -> str:
        return str(self)
