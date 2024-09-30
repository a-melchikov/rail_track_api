from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from schemas.train_type import TrainTypeCreate, TrainTypeOut
from utils.service import BaseService


class TrainTypeService(BaseService):
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
