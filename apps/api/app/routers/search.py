from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import status

from ..core import Video
from ..core import YouTubeGetVideo
from ..core import YouTubeSearch
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
def get_search(session: DependsSession, query: str) -> list[Video]:
    session.search = YouTubeSearch(query)
    videos = session.search.results
    if len(videos) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return videos


@router.get('/next')
def get_next_search(session: DependsSession) -> list[Video]:
    if session.search is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    else:
        has_more = session.search.next()
        if not has_more:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        else:
            videos = session.search.results
            if len(videos) == 0:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
            else:
                return videos


@router.get('/video')
def get_video(session: DependsSession, id: str) -> Video:
    video = YouTubeGetVideo(id).result
    if video is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return video
