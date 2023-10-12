import json
from typing import Any

from ..models import Channel
from ..models import Video
from .core import VideosSearch


class YouTubeVideoSearch:
    def __init__(self, term: str):
        self._term = term

    def results(self) -> list[Video]:
        try:
            results = VideosSearch(self._term).result()
            if isinstance(results, str):
                results = json.loads(results)
            videos = results.get('result', [])
            return [self.format_search_result(video) for video in videos]
        except KeyError:
            return []

    def format_search_result(self, result: dict[str, Any]) -> Video:
        duration = result.get('duration', None)
        if duration is None:
            duration = '--:--'
        return Video(
            id=result['id'],
            url=result['link'],
            title=result['title'],
            duration=duration,
            thumbnail=result['thumbnails'][0]['url'],
            channel=Channel(
                name=result['channel']['name'],
                url=result['channel']['link'],
                thumbnail=result['channel']['thumbnails'][0]['url'],
            ),
        )
