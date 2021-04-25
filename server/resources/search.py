from flask import jsonify, Blueprint, request
from youtube_dl import YoutubeDL

http = Blueprint(r"http_search", __name__)

DEFAULT_SEARCH_RESULT_SIZE = 5
YOUTUBE_DL_SEARCH_OPTIONS = {
    "noplaylist": True,
    "quiet": True,
}

@http.route("/search")
def search(self):
    search_term = request.args.get("term")
    results_size = request.args.get("results", DEFAULT_SEARCH_RESULT_SIZE)
    with YoutubeDL(YOUTUBE_DL_SEARCH_OPTIONS) as ydl:
        videos = ydl.extract_info(
            f"ytsearch{results_size}:{search_term}", download=False
        )["entries"]
        return jsonify(videos)
