from typing import TYPE_CHECKING

from sqlalchemy import String, CHAR, ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import Base


if TYPE_CHECKING:
    from db import Address


class Station(Base):
    name: Mapped[str] = mapped_column(String(255))
    tax_id: Mapped[str] = mapped_column(CHAR(12), unique=True)
    address_id: Mapped[int] = mapped_column(
        ForeignKey("addresses.id", ondelete="CASCADE"),
        unique=True,
    )
    address: Mapped["Address"] = relationship(
        back_populates="stations",
    )
    __table_args__ = (
        CheckConstraint(
            "length(tax_id)=12",
            name="check_tax_id_length",
        ),
    )

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id}, name={self.name}, tax_id={self.tax_id}, address_id={self.address_id})"

    def __repr__(self) -> str:
        return str(self)
