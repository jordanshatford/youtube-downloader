from flask import jsonify, Blueprint, request
from youtube_dl import YoutubeDL
from youtube_dl.utils import match_filter_func


http = Blueprint(r"http_search", __name__)


@http.route("/search", methods=["GET"])
def search():
    term, size = get_search_request_args(request)
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
        return jsonify(videos)


def get_search_request_args(request):
    search_term = request.args.get("term")
    results_size = request.args.get("results", 5)
    return search_term, results_size
