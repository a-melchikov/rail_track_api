from pydantic import BaseModel, ConfigDict


class AddressBase(BaseModel):
    country: str
    city: str
    street: str
    house: str
    apartment: str


class AddressCreate(AddressBase):
    pass


class AddressUpdate(AddressBase):
    pass


class AddressOut(AddressBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
