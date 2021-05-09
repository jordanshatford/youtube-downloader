from youtube_search import YoutubeSearch


YOUTUBE_URL_PREFIX = "https://www.youtube.com/"


def search_youtube(term: str, results: int) -> list:
    results = YoutubeSearch(term, max_results=int(results))
    videos = results.to_dict()
    return [format_search_result(video) for video in videos]


def format_search_result(result: dict) -> dict:
    return {
        "id": result["id"],
        "url": YOUTUBE_URL_PREFIX + result["url_suffix"],
        "title": result["title"],
        "thumbnail": result["thumbnails"][0],
        "description": result["long_desc"] if result["long_desc"] else "",
        "channel": result["channel"],
        "duration": result["duration"]
    }
