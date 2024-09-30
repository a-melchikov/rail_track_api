from abc import ABC, abstractmethod

from pydantic import BaseModel
from sqlalchemy import delete, select, update

from db import db_helper, Base


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one(self, model_in: BaseModel) -> BaseModel:
        raise NotImplementedError

    @abstractmethod
    async def find_all(self) -> list[BaseModel]:
        raise NotImplementedError

    @abstractmethod
    async def find_one(self, **filter_by) -> BaseModel:
        raise NotImplementedError

    @abstractmethod
    async def update_one(self, id: int, model_update: BaseModel) -> BaseModel:
        raise NotImplementedError

    @abstractmethod
    async def delete_one(self, id: int) -> None:
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model: Base
    schema: BaseModel

    async def add_one(self, model_in: BaseModel) -> BaseModel:
        """Создает новую запись и возвращает ее"""
        async with db_helper.session_factory() as session:
            model_obj = self.model(**model_in.model_dump())
            session.add(model_obj)
            await session.commit()
            return self.schema.model_validate(model_obj, from_attributes=True)

    async def find_all(self) -> list[BaseModel]:
        """Возвращает все записи из таблицы"""
        async with db_helper.session_factory() as session:
            stmt = select(self.model).order_by(self.model.id)
            result = await session.execute(stmt)
            models_obj = result.scalars().all()
            return [
                self.schema.model_validate(obj, from_attributes=True)
                for obj in models_obj
            ]

    async def find_one(self, **filter_by) -> BaseModel:
        """Возвращает одну запись, соответствующую фильтру"""
        async with db_helper.session_factory() as session:
            stmt = select(self.model).filter_by(**filter_by)
            result = await session.execute(stmt)
            model_obj = result.scalar_one_or_none()

            if result is None:
                raise ValueError(f"Record not found for filter: {filter_by}")

            return self.schema.model_validate(model_obj, from_attributes=True)

    async def update_one(self, id: int, model_update: BaseModel) -> BaseModel:
        """Обновляет запись по ее id"""
        async with db_helper.session_factory() as session:
            stmt = (
                update(self.model)
                .where(self.model.id == id)
                .values(**model_update.model_dump(exclude_unset=True))
                .returning(self.model)
            )
            result = await session.execute(stmt)
            await session.commit()
            model_obj = result.scalar_one_or_none()

            if model_obj is None:
                raise ValueError(f"Record with id {id} not found")

            return self.schema.model_validate(model_obj, from_attributes=True)

    async def delete_one(self, id: int) -> None:
        """Удаляет запись по её id и возвращает id удалённой записи"""
        async with db_helper.session_factory() as session:
            stmt = delete(self.model).where(self.model.id == id)
            res = await session.execute(stmt)
            await session.commit()

            if res.rowcount == 0:
                raise ValueError(f"Record with id {id} not found")
