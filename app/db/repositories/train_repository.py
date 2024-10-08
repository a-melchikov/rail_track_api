from db.models.train import Train
from schemas.train import TrainOut, TrainRelOut
from utils.repository import SQLAlchemyRepository


class TrainRepository(SQLAlchemyRepository):
    model = Train
    schema = TrainOut
    schema_rel = TrainRelOut

    