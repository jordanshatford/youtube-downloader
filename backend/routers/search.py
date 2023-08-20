from fastapi import APIRouter
from utils.models import Video
from utils.youtube import search_youtube

router = APIRouter()


@router.get('/search', tags=['search'], response_model=list[Video])
def get_search(term: str, results: int = 12):
    return search_youtube(term, results)
