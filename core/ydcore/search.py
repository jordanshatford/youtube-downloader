import json
from typing import Any

from youtubesearchpython import VideosSearch

from .models import Channel
from .models import Video

DEFAULT_SEARCH_RESULTS_LIMIT = 12


class YouTubeVideoSearch:
    def __init__(self, term: str, limit: int = DEFAULT_SEARCH_RESULTS_LIMIT):
        self._term = term
        self._limit = limit

    def results(self) -> list[Video]:
        try:
            results = VideosSearch(self._term, limit=self._limit).result()
            if isinstance(results, str):
                results = json.loads(results)
            videos = results.get('result', [])
            return [self.format_search_result(video) for video in videos]
        except KeyError:
            return []

    def format_search_result(self, result: dict[str, Any]) -> Video:
        return Video(
            id=result['id'],
            url=result['link'],
            title=result['title'],
            duration=result['duration'],
            thumbnail=result['thumbnails'][0]['url'],
            channel=Channel(
                name=result['channel']['name'],
                url=result['channel']['link'],
                thumbnail=result['channel']['thumbnails'][0]['url'],
            ),
        )
