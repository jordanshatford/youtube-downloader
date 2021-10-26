from youtubesearchpython import VideosSearch


def search_youtube(term: str, results_size: int) -> list:
    try:
        results = VideosSearch(term, limit=int(results_size))
        videos = results.result()["result"]
        return [format_search_result(video) for video in videos]
    except KeyError:
        return []


def format_search_result(result: dict) -> dict:
    return {
        "id": result["id"],
        "url": result["link"],
        "title": result["title"],
        "duration": result["duration"],
        "thumbnail": result["thumbnails"][0]["url"],
        "channel": result["channel"]["name"],
        "channelUrl": result["channel"]["link"],
        "channelThumbnail": result["channel"]["thumbnails"][0]["url"],
    }
