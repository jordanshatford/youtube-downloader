from fastapi import APIRouter
from utils.managers import session_manager
from utils.models import Session

router = APIRouter()


@router.get('/session', tags=['session'])
def get_session() -> Session:
    session_id = session_manager.create()
    return Session(id=session_id)
