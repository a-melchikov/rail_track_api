from pydantic import BaseModel, ConfigDict, Field


class TrainTypeBase(BaseModel):
    type_name: str = Field(..., max_length=100)


class TrainTypeCreate(TrainTypeBase):
    pass


class TrainTypeUpdate(BaseModel):
    type_name: str | None = Field(None, max_length=100)


class TrainTypeOut(TrainTypeBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
