from fastapi import APIRouter
from yad_api.utils.managers import session_manager
from yad_api.utils.models import Session

router = APIRouter(
    prefix='/session',
    tags=['session'],
)


@router.get('')
def get_session() -> Session:
    session_id = session_manager.create()
    return Session(id=session_id)
