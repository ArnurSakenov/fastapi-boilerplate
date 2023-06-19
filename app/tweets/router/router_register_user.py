from fastapi import Depends, Response

from app.utils import AppModel

from ..service import Service, get_service
from . import router


class CreateTweetRequest(AppModel):
    content: str


@router.post("/")
def create_tweet(
    input: CreateTweetRequest,
    svc: Service = Depends(get_service),
) -> dict[str, str]:
    svc.repository.create_tweet(input.dict())

    return Response(status_code=200)
