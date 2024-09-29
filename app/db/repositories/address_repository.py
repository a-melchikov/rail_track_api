import asyncio

from db import db_helper, Address
from schemas.address import AddressOut
from utils.repository import SQLAlchemyRepository


class AddressRepository(SQLAlchemyRepository):
    model = Address
    schema = AddressOut


async def main():
    async with db_helper.session_factory() as session:
        address_repo = AddressRepository(session=session)

        # # 1. Создание адреса
        # new_address_data = AddressCreate(
        #     country="Russia",
        #     city="Moscow",
        #     street="Tverskaya",
        #     house="6",
        #     apartment="12A",
        # )
        # new_address = await address_repo.create_address(new_address_data)
        # print("Созданный адрес:", new_address)

        # # 2. Получение всех адресов
        # all_addresses = await address_repo.get_all_addresses()
        # print("Список всех адресов:", all_addresses)

        # 3. Получение адреса по ID
        # _id = 7
        # address_by_id = await address_repo.get_address_by_id(_id)
        # print(f"Полученный адрес с ID {_id}:", address_by_id)

        # 4. Обновление адреса
        # _id = 7
        # address_by_id = await address_repo.get_address_by_id(_id)
        # update_data = AddressUpdate(
        #     country="Russia",
        #     city="Moscow",
        #     street="Tverskaya",
        #     house="100",  # Изменение номера дома
        #     apartment="12A",
        # )
        # updated_address = await address_repo.update_address(address_by_id, update_data) # type: ignore
        # print("Обновленный адрес:", updated_address)

        # 5. Удаление адреса
        # _id = 7
        # updated_address = await address_repo.get_address_by_id(_id)
        # await address_repo.delete_address(updated_address) # type: ignore
        # print(f"Адрес с ID {_id} удален.")

        # 6. Проверка, что адрес удален
        # _id = 7
        # deleted_address_check = await address_repo.get_address_by_id(_id)
        # print(f"Попытка получить удаленный адрес с ID {_id}: {deleted_address_check}")


if __name__ == "__main__":
    asyncio.run(main())
