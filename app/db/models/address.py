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
