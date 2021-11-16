import uuid

from fastapi import APIRouter
from fastapi import Response
from utils.managers import session_manager
from utils.models import Message

router = APIRouter()


@router.get("/session", tags=["session"], response_model=Message)
def get_session(response: Response):
    session_id = str(uuid.uuid4())
    session_manager.setup_session(session_id)
    response.set_cookie(
        key="session_id", value=session_id, samesite="none", secure=True
    )
    return {
        "title": "Session Created",
        "message": "The session has been successfully created and setup.",
    }
