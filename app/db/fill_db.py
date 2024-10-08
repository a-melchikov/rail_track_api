import asyncio
import random

from faker import Faker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select

from db import Address, Station, Train, TrainType, TrainStationAssociation
from db.session import db_helper

fake = Faker()


async def create_random_addresses(num: int, session: AsyncSession):
    addresses = []
    for _ in range(num):
        addresses.append(
            Address(
                country=fake.country(),
                city=fake.city(),
                street=fake.street_name(),
                house=str(fake.building_number()),
                apartment=(
                    str(fake.random_int(min=1, max=100))
                    if fake.random_int(min=0, max=1)
                    else None
                ),
            )
        )
    session.add_all(addresses)
    await session.commit()


async def create_random_train_types(num: int, session: AsyncSession):
    train_types = []
    for _ in range(num):
        train_types.append(TrainType(type_name=fake.word() + " Train"))
    session.add_all(train_types)
    await session.commit()


async def create_random_stations(num: int, session: AsyncSession):
    addresses = await session.execute(select(Address))
    addresses = addresses.scalars().all()

    if len(addresses) < num:
        raise ValueError(
            f"Не достаточно уникальных адресов для создания {num} станций."
        )

    selected_addresses = random.sample(addresses, num)
    stations = []

    for address in selected_addresses:
        tax_id = str(fake.unique.random_number(digits=12)).zfill(
            12
        )
        station = Station(
            name=fake.company() + " Station",
            tax_id=tax_id,
            address_id=address.id,
        )

        try:
            stations.append(station)
        except IntegrityError:
            print(f"Пропущена дублирующаяся запись для address_id={address.id}")

    session.add_all(stations)
    await session.commit()


async def create_random_trains(num: int, session: AsyncSession):
    train_types_result = await session.execute(select(TrainType))
    train_types = train_types_result.scalars().all()

    stations_result = await session.execute(select(Station))
    stations = stations_result.scalars().all()

    trains = []
    for _ in range(num):
        train_type = random.choice(train_types)
        station = random.choice(stations)
        trains.append(
            Train(
                name=fake.word() + " Express",
                train_type_id=train_type.id,
                station_id=station.id,
            )
        )
    session.add_all(trains)
    await session.commit()


async def create_random_train_stations(num: int, session: AsyncSession):
    trains_result = await session.execute(select(Train))
    trains = trains_result.scalars().all()

    stations_result = await session.execute(select(Station))
    stations = stations_result.scalars().all()

    train_stations = []

    for train in trains:
        num_stations = random.randint(1, len(stations) // 2)
        assigned_stations = random.sample(stations, num_stations)

        for station in assigned_stations:
            train_stations.append(
                TrainStationAssociation(train_id=train.id, station_id=station.id)
            )

    session.add_all(train_stations)
    await session.commit()


async def main():
    async with db_helper.session_factory() as session:
        await create_random_addresses(10, session)
        await create_random_stations(5, session)
        await create_random_train_types(3, session)
        await create_random_trains(10, session)
        await create_random_train_stations(10, session)


if __name__ == "__main__":
    asyncio.run(main())
