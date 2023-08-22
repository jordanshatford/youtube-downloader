from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import status
from utils.models import Video
from utils.youtube import search_youtube

router = APIRouter(
    prefix='/search',
    tags=['search'],
    responses={
        status.HTTP_404_NOT_FOUND: {},
    },
)


@router.get('')
def get_search(term: str, results: int = 12) -> list[Video]:
    videos = search_youtube(term, results)
    if len(videos) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return videos
