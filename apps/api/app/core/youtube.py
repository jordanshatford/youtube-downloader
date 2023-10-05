import json
from typing import Any

from pydantic import HttpUrl
from youtubesearchpython import VideosSearch

from ..models import Channel
from ..models import Video


def search_youtube(term: str, results_size: int) -> list[Video]:
    try:
        results = VideosSearch(term, limit=int(results_size)).result()
        if isinstance(results, str):
            results = json.loads(results)
        videos = results.get('result', [])
        return [format_search_result(video) for video in videos]
    except KeyError:
        return []


def format_search_result(result: dict[str, Any]) -> Video:
    channel = Channel(
        name=result['channel']['name'],
        url=HttpUrl(result['channel']['link']),
        thumbnail=HttpUrl(
            result['channel']['thumbnails'][0]['url'],
        ),
    )
    return Video(
        id=result['id'],
        url=HttpUrl(result['link']),
        title=result['title'],
        duration=result['duration'],
        thumbnail=HttpUrl(result['thumbnails'][0]['url']),
        channel=channel,
    )
