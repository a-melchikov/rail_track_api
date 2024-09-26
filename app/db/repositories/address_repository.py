import asyncio

from sqlalchemy.ext.asyncio import AsyncSession
from db import Address, db_helper


class AddressRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_address(
        self,
        country: str,
        city: str,
        street: str | None,
        house: str,
        apartment: str,
    ) -> Address:
        address = Address(
            country=country,
            city=city,
            street=street,
            house=house,
            apartment=apartment,
        )
        self.session.add(address)
        await self.session.commit()
        return address


async def main():
    async with db_helper.session_factory() as session:
        address_repo = AddressRepository(session=session)

        addresses_data = [
            ("Russia", "Moscow", "Tverskaya", "6", "12A"),
            ("Russia", "Saint Petersburg", "Nevsky Prospect", "45", "2"),
            ("Russia", "Novosibirsk", "Red Avenue", "20", "5"),
            ("Russia", "Yekaterinburg", "Lenin Street", "10", "1"),
            ("Russia", "Kazan", "Bauman Street", "15", "3"),
        ]

        for data in addresses_data:
            await address_repo.create_address(*data)

        await session.commit()


if __name__ == "__main__":
    asyncio.run(main())
