from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from db.base import Base


class Address(Base):
    __tablename__ = "addresses"

    country: Mapped[str] = mapped_column(String(100))
    city: Mapped[str] = mapped_column(String(100))
    street: Mapped[str | None] = mapped_column(String(255))
    house: Mapped[str | None] = mapped_column(String(10))
    apartment: Mapped[str | None] = mapped_column(String(10))

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(country={self.country}, city={self.city},street={self.street}, house={self.house}, apartment={self.apartment})"

    def __repr__(self) -> str:
        return str(self)
