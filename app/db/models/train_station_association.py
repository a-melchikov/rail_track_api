from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from db import Base


class TrainStationAssociation(Base):
    __tablename__ = "train_station_association"

    train_id: Mapped[int] = mapped_column(
        ForeignKey("trains.id", ondelete="CASCADE"), primary_key=True
    )
    station_id: Mapped[int] = mapped_column(
        ForeignKey("stations.id", ondelete="CASCADE"), primary_key=True
    )

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(train_id={self.train_id}, station_id={self.station_id})"

    def __repr__(self) -> str:
        return str(self)
