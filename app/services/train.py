from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError

from db.repositories import TrainRepository
from schemas.train import TrainCreate, TrainOut, TrainRelOut
from utils.service import BaseService


class TrainService(BaseService):
    repo: TrainRepository

    async def create_train(self, train_in: TrainCreate) -> TrainOut:
        try:
            train = await self.repo.add_one(train_in)
            return train
        except SQLAlchemyError as e:
            raise HTTPException(
                status_code=500,
                detail="An unexpected error occurred while creating the train.",
            ) from e
