import uuid

from fastapi import APIRouter
from utils.managers import session_manager
from utils.models import Session

router = APIRouter()


@router.get('/session', tags=['session'], response_model=Session)
def get_session():
    session_id = str(uuid.uuid4())
    session_manager.setup_session(session_id)
    return Session(id=session_id)
