from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import status

from app.core import SearchState
from app.core import Video
from app.dependencies import DependsSession
from app.dependencies import depends_session_responses

router = APIRouter(
    prefix="/search",
    tags=["search"],
    responses=depends_session_responses
    | {
        status.HTTP_404_NOT_FOUND: {},
    },
)


@router.get("")
def get_search(session: DependsSession, query: str) -> list[Video]:
    videos = session.search.get(query)
    if len(videos) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return videos


@router.get("/state")
def get_search_state(session: DependsSession) -> SearchState:
    return SearchState(query=session.search.query, results=session.search.results)


@router.get("/next")
def get_search_next(session: DependsSession) -> list[Video]:
    if not session.search.has_more:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    videos = session.search.get_next()
    if len(videos) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return videos
