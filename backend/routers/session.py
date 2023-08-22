from fastapi import APIRouter
from utils.managers import session_manager
from utils.models import Session

router = APIRouter(
    prefix='/session',
    tags=['session'],
)


@router.get('')
def get_session() -> Session:
    session_id = session_manager.create()
    return Session(id=session_id)
