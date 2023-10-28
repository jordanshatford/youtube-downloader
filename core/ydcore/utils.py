from pydantic import HttpUrl
from pydantic import ValidationError

from .models import Video
from .search import YouTubeSearch


def is_valid_url(url: str) -> bool:
    try:
        HttpUrl(url)
        return True
    except ValidationError:
        return False


def get_video_from_url(url: str | HttpUrl) -> Video | None:
    url = str(url)
    if not is_valid_url(url):
        return None
    results = YouTubeSearch(url).results
    return next((v for v in results if v.url == HttpUrl(url)), None)
