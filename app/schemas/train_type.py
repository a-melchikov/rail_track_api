from pydantic import BaseModel, ConfigDict


class TrainTypeBase(BaseModel):
    type_name: str


class TrainTypeCreate(TrainTypeBase):
    pass


class TrainTypeUpdate(BaseModel):
    type_name: str | None = None


class TrainTypeOut(TrainTypeBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
