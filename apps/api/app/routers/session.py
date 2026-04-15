from fastapi import APIRouter
from fastapi import status

from app.dependencies import DependsSession
from app.dependencies import depends_session_responses
from app.models import Session
from app.session import session_manager

router = APIRouter(tags=["session"])


@router.get("/session")
def get_session() -> Session:
    session_id = session_manager.create()
    return Session(id=session_id)


@router.delete(
    "/session",
    status_code=status.HTTP_204_NO_CONTENT,
    responses=depends_session_responses,
)
def delete_session(session: DependsSession) -> None:
    session_manager.remove(session.id)


@router.get("/session/validate", responses=depends_session_responses)
def get_session_validate(session: DependsSession) -> Session:
    return Session(id=session.id)
