from db import TrainType
from schemas.train_type import TrainTypeOut
from utils.repository import SQLAlchemyRepository


class TrainTypeRepository(SQLAlchemyRepository):
    model = TrainType
    schema = TrainTypeOut
