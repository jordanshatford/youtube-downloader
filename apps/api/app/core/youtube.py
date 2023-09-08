import json
from typing import Any

from pydantic import HttpUrl
from pydantic import parse_obj_as
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
        url=parse_obj_as(HttpUrl, result['channel']['link']),
        thumbnail=parse_obj_as(
            HttpUrl, result['channel']['thumbnails'][0]['url'],
        ),
    )
    return Video(
        id=result['id'],
        url=parse_obj_as(HttpUrl, result['link']),
        title=result['title'],
        duration=result['duration'],
        thumbnail=parse_obj_as(HttpUrl, result['thumbnails'][0]['url']),
        channel=channel,
    )
