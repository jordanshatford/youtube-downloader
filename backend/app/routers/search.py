from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import status

from ..dependencies import depends_session_responses
from ..dependencies import DependsSession
from ..models import Video
from ..utils.youtube import search_youtube

router = APIRouter(
    prefix='/search',
    tags=['search'],
    responses={
        **depends_session_responses,
        status.HTTP_404_NOT_FOUND: {},
    },
)


@router.get('')
def get_search(session: DependsSession, term: str, results: int = 12) -> list[Video]:  # noqa: E501
    session.update_use_time()
    videos = search_youtube(term, results)
    if len(videos) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return videos
