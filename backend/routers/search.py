from fastapi import APIRouter
from utils.models import Video
from utils.youtube import search_youtube

router = APIRouter()


@router.get('/search', tags=['search'])
def get_search(term: str, results: int = 12) -> list[Video]:
    return search_youtube(term, results)
