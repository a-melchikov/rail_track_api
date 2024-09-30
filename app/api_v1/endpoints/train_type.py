from typing import Annotated
from fastapi import APIRouter, Depends, status

from api_v1.dependencies import train_type_service_dependency
from schemas.train_type import TrainTypeCreate, TrainTypeOut
from services.train_type import TrainTypeService

router = APIRouter()


@router.post("/", response_model=TrainTypeOut, status_code=status.HTTP_201_CREATED)
async def create_train_type(
    train_type_in: TrainTypeCreate,
    train_type_service: train_type_service_dependency,
) -> TrainTypeOut:
    return await train_type_service.create_train_type(train_type_in=train_type_in)


@router.get("/", response_model=list[TrainTypeOut])
async def get_train_types(
    train_type_service: train_type_service_dependency,
) -> list[TrainTypeOut]:
    return await train_type_service.get_all_train_types()


@router.delete(
    "/{train_type_id}", response_model=None, status_code=status.HTTP_204_NO_CONTENT
)
async def delete_train_type(
    train_type_id: int,
    train_type_service: train_type_service_dependency,
) -> None:
    await train_type_service.delete_train_type(train_type_id=train_type_id)
