from pydantic import HttpUrl

from .models import Video
from .search import YouTubeSearch


def get_video_from_url(url: str | HttpUrl) -> Video | None:
    url = str(HttpUrl)
    results = YouTubeSearch(url).results
    return next((v for v in results if v.url == HttpUrl(url)), None)

