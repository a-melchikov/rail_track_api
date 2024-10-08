from pydantic import BaseModel, ConfigDict, Field

from schemas.train_type import TrainTypeOut


class TrainBase(BaseModel):
    name: str = Field(..., max_length=255)
    train_type_id: int


class TrainCreate(TrainBase):
    pass


class TrainUpdate(BaseModel):
    name: str | None = Field(None, max_length=255)
    train_type_id: int | None = None


class TrainOut(TrainBase):
    model_config = ConfigDict(from_attributes=True)
    id: int


class TrainRelOut(TrainOut):
    train_type: TrainTypeOut
