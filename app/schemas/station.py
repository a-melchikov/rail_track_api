from pydantic import BaseModel, ConfigDict, Field

from schemas.address import AddressOut


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


class StationOut(StationBase):
    model_config = ConfigDict(from_attributes=True)
    id: int


class StationRelOut(StationOut):
    address: AddressOut
