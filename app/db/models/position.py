from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from db import Base
from db.mixins import IdMixin


class Position(IdMixin, Base):
    position_name: Mapped[str] = mapped_column(String(100), unique=True)

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id}, position_name={self.position_name})"

    def __repr__(self) -> str:
        return str(self)
