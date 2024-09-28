from pydantic import BaseModel, ConfigDict, Field


class StationBase(BaseModel):
    name: str = Field(..., max_length=255)
    tax_id: str = Field(..., min_length=12, max_length=12)
    address_id: int


class StationCreate(StationBase):
    pass


class StationUpdate(BaseModel):
    name: str | None = Field(None, max_length=255)
    tax_id: str | None = Field(None, min_length=12, max_length=12)
    address_id: int | None = None


class Station(StationBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
