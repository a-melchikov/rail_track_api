from pydantic import BaseModel, ConfigDict


class AddressBase(BaseModel):
    country: str
    city: str
    street: str
    house: str
    apartment: str


class AddressCreate(AddressBase):
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "country": "Russia",
                    "city": "Moscow",
                    "street": "Lenin Street",
                    "house": "1A",
                    "apartment": "1",
                },
            ]
        }
    }


class AddressUpdate(BaseModel):
    country: str | None = None
    city: str | None = None
    street: str | None = None
    house: str | None = None
    apartment: str | None = None


class AddressOut(AddressBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
