from fastapi import APIRouter
from fastapi import status

from ..dependencies import depends_session_responses
from ..dependencies import DependsSession
from ..models import Session
from ..session import session_manager

router = APIRouter(
    prefix='/session',
    tags=['session'],
)


@router.get('')
def get_session() -> Session:
    session_id = session_manager.create()
    return Session(id=session_id)


@router.delete(
    '', status_code=status.HTTP_204_NO_CONTENT,
    responses=depends_session_responses,
)
def delete_session(session: DependsSession) -> None:
    session_manager.remove(session.id)
