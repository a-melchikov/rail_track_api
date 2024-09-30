from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from db import Base


class TrainType(Base):
    __tablename__ = "train_types"

    type_name: Mapped[str] = mapped_column(String(100), unique=True)

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id}, type_name={self.type_name}"

    def __repr__(self) -> str:
        return str(self)
