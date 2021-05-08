from flask import jsonify, Blueprint, request
from youtube_dl import YoutubeDL
from youtube_dl.utils import match_filter_func, DownloadError


http = Blueprint(r"http_search", __name__)


@http.route("/search", methods=["GET"])
def search():
    term, size = get_search_request_args(request)

    try:
        with YoutubeDL(
            {
                "noplaylist": True,
                "quiet": True,
                "match_filter": match_filter_func("!is_live"),
            }
        ) as ydl:
            videos = ydl.extract_info(f"ytsearch{size}:{term}", download=False).get(
                "entries", []
            )
            return jsonify([format_result(video) for video in videos])
    except DownloadError:
        return jsonify([])


def get_search_request_args(request):
    search_term = request.args.get("term")
    results_size = request.args.get("results", 5)
    return search_term, results_size


def format_result(result):
    return {
        "id": result["id"],
        "url": result["webpage_url"],
        "title": result["title"],
        "thumbnail": result["thumbnail"],
        "description": result["description"],
        "channel_url": result["channel_url"],
        "channel": result["channel"],
        "duration": result["duration"]
    }