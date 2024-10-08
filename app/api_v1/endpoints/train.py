from fastapi import APIRouter, status

from schemas.train import TrainCreate, TrainOut
from api_v1.dependencies import train_service_dependency

router = APIRouter()


@router.post("/", response_model=TrainOut, status_code=status.HTTP_201_CREATED)
async def create_train(
    train_in: TrainCreate,
    train_service: train_service_dependency,
) -> TrainOut:
    return await train_service.create_train(train_in=train_in)
