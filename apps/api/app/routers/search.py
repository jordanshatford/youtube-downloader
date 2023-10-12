from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import status
from ydcore import Video
from ydcore import YouTubeVideoSearch

from ..dependencies import depends_session_responses
from ..dependencies import DependsSession

router = APIRouter(
    prefix='/search',
    tags=['search'],
    responses=depends_session_responses | {
        status.HTTP_404_NOT_FOUND: {},
    },
)


@router.get('')
def get_search(session: DependsSession, term: str) -> list[Video]:
    session.update_use_time()
    videos = YouTubeVideoSearch(term).results()
    if len(videos) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return videos
