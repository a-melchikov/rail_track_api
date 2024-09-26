from pydantic import BaseModel, ConfigDict


class AddressBase(BaseModel):
    country: str
    city: str
    street: str
    house: str
    apartment: str


class AddressCreate(AddressBase):
    pass


class Address(AddressBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
