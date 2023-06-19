
from app.config import database

from .repository.repository import TweetsRepository


class Service:
    def __init__(
        self,
        repository: TweetsRepository,
    ):
        self.repository = repository


def get_service():
    repository = TweetsRepository(database)
    svc = Service(repository)
    return svc
