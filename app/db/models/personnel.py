from typing import TYPE_CHECKING

from sqlalchemy import String, CHAR, ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db import Base

if TYPE_CHECKING:
    from db import Station, Position, CrewDirectory


class Personnel(Base):
    __tablename__ = "personnel"
    __table_args__ = (
        CheckConstraint(
            "length(person_tax_id)=12",
            name="check_person_tax_id_length",
        ),
    )

    person_tax_id: Mapped[str] = mapped_column(
        CHAR(12),
        primary_key=True,
    )
    station_id: Mapped[int] = mapped_column(
        ForeignKey("stations.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    position_id: Mapped[int] = mapped_column(ForeignKey("positions.id"))
    crew_id: Mapped[int] = mapped_column(ForeignKey("crew_directories.id"))
    full_name: Mapped[str] = mapped_column(String(255))

    station: Mapped["Station"] = relationship(back_populates="personnel")
    position: Mapped["Position"] = relationship(back_populates="personnel")
    crew: Mapped["CrewDirectory"] = relationship(back_populates="personnel")

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(station_id={self.station_id}, person_tax_id={self.person_tax_id}, full_name={self.full_name}, position_id={self.position_id}, crew_id={self.crew_id})"

    def __repr__(self) -> str:
        return str(self)
