from abc import ABC, abstractmethod

from sqlalchemy import delete, insert, select, update

from db import db_helper


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one(self, data: dict) -> dict:
        raise NotImplementedError

    @abstractmethod
    async def find_all(self) -> list:
        raise NotImplementedError

    @abstractmethod
    async def find_one(self, **filter_by) -> dict:
        raise NotImplementedError

    @abstractmethod
    async def update_one(self, id: int, data: dict) -> dict:
        raise NotImplementedError

    @abstractmethod
    async def delete_one(self, id: int) -> None:
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def add_one(self, data: dict) -> dict:
        """Создает новую запись и возвращает ее"""
        async with db_helper.session_factory() as session:
            columns = [col for col in self.model.__table__.columns]

            stmt = insert(self.model).values(**data).returning(*columns)
            res = await session.execute(stmt)
            await session.commit()
            return res.mappings().one()

    async def find_all(self) -> list[dict]:
        """Возвращает все записи из таблицы"""
        async with db_helper.session_factory() as session:
            stmt = select(self.model).order_by(self.model.id)
            res = await session.execute(stmt)
            return [
                {
                    column: getattr(row.Address, column)
                    for column in row.Address.__table__.columns.keys()
                }
                for row in res.all()
            ]

    async def find_one(self, **filter_by) -> dict:
        """Возвращает одну запись, соответствующую фильтру"""
        async with db_helper.session_factory() as session:
            stmt = select(self.model).filter_by(**filter_by)
            res = await session.execute(stmt)
            result = res.mappings().one_or_none()
            
            if result is None:
                raise ValueError(f"Record not found for filter: {filter_by}")
            extracted_result = result["Address"].__dict__ if "Address" in result else result

            return extracted_result

    async def update_one(self, id: int, data: dict) -> dict:
        """Обновляет запись по ее id"""
        async with db_helper.session_factory() as session:
            columns = [col for col in self.model.__table__.columns]
            stmt = (
                update(self.model)
                .where(self.model.id == id)
                .values(**data)
                .returning(*columns)
            )
            res = await session.execute(stmt)
            await session.commit()
            result = res.mappings().one_or_none()

            if result is None:
                raise ValueError(f"Record with id {id} not found")

            return result

    async def delete_one(self, id: int) -> None:
        """Удаляет запись по её id и возвращает id удалённой записи"""
        async with db_helper.session_factory() as session:
            stmt = delete(self.model).where(self.model.id == id)
            res = await session.execute(stmt)
            await session.commit()

            if res.rowcount == 0:
                raise ValueError(f"Record with id {id} not found")
