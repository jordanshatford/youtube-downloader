from typing import List

from youtubesearchpython import VideosSearch

from .models import Channel
from .models import Video


def search_youtube(term: str, results_size: int) -> List[Video]:
    try:
        results = VideosSearch(term, limit=int(results_size))
        videos = results.result()['result']
        return [format_search_result(video) for video in videos]
    except KeyError:
        return []


def format_search_result(result: dict) -> Video:
    return Video(
        id=result['id'],
        url=result['link'],
        options=None,
        title=result['title'],
        duration=result['duration'],
        thumbnail=result['thumbnails'][0]['url'],
        channel=Channel(
            name=result['channel']['name'],
            url=result['channel']['link'],
            thumbnail=result['channel']['thumbnails'][0]['url'],
        ),
    )
