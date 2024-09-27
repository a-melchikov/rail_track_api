from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.base import Base

if TYPE_CHECKING:
    from db import Station


class Address(Base):
    __tablename__ = "addresses"

    country: Mapped[str] = mapped_column(String(100))
    city: Mapped[str] = mapped_column(String(100))
    street: Mapped[str | None] = mapped_column(String(255))
    house: Mapped[str | None] = mapped_column(String(10))
    apartment: Mapped[str | None] = mapped_column(String(10))

    stations: Mapped["Station"] = relationship(
        back_populates="address",
        cascade="all, delete",
    )

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id}, country={self.country}, city={self.city},street={self.street}, house={self.house}, apartment={self.apartment})"

    def __repr__(self) -> str:
        return str(self)
