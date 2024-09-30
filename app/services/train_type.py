from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db.repositories.train_type_repository import TrainTypeRepository
from schemas.train_type import TrainTypeCreate, TrainTypeOut
from utils.service import BaseService


class TrainTypeService(BaseService):
    repo: TrainTypeRepository

    async def create_train_type(
        self,
        train_type_in: TrainTypeCreate,
    ) -> TrainTypeOut:
        try:
            train_type = await self.repo.add_one(train_type_in)
            return train_type
        except IntegrityError as e:
            if "train_types_type_name_key" in str(e.orig):
                raise HTTPException(
                    status_code=409,
                    detail=f"Train type with name '{train_type_in.type_name}' already exists.",
                ) from e
            raise HTTPException(
                status_code=400, detail="A database integrity error occurred."
            ) from e
        except SQLAlchemyError as e:
            raise HTTPException(
                status_code=500,
                detail="An unexpected error occurred while creating the train type.",
            ) from e

    async def get_all_train_types(
        self,
    ) -> list[TrainTypeOut]:
        try:
            train_types = await self.repo.find_all()
            return train_types
        except SQLAlchemyError as e:
            raise HTTPException(
                status_code=500,
                detail="An unexpected error occurred while getting all train types.",
            ) from e

    async def delete_train_type(
        self,
        train_type_id: int,
    ) -> None:
        try:
            await self.repo.delete_one(train_type_id)
        except ValueError as e:
            raise HTTPException(
                status_code=404, detail=f"Train type with id {train_type_id} not found"
            ) from e
        except SQLAlchemyError as e:
            raise HTTPException(
                status_code=500,
                detail="An unexpected error occurred while deleting the train type.",
            ) from e
