from utils.repository import AbstractRepository


class BaseService:
    def __init__(self, repo: AbstractRepository):
        self.repo = repo()
