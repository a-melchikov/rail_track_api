from typing import Annotated
from fastapi import APIRouter, Depends, status

from api_v1.dependencies import train_type_service
from schemas.train_type import TrainTypeCreate, TrainTypeOut
from services.train_type import TrainTypeService

router = APIRouter()


@router.post("/", response_model=TrainTypeOut, status_code=status.HTTP_201_CREATED)
async def create_address(
    train_type_in: TrainTypeCreate,
    train_type_service: Annotated[TrainTypeService, Depends(train_type_service)],
) -> TrainTypeOut:
    return await train_type_service.create_train_type(train_type_in=train_type_in)
