from flask import jsonify, request
from flask_restful import Resource
from youtube_dl import YoutubeDL


DEFAULT_SEARCH_RESULT_SIZE = 5
YOUTUBE_DL_SEARCH_OPTIONS = {
    "noplaylist": True,
    "quiet": True,
}


class Search(Resource):
    def get(self):
        search_term = request.args.get("term")
        results_size = request.args.get("results", DEFAULT_SEARCH_RESULT_SIZE)
        with YoutubeDL(YOUTUBE_DL_SEARCH_OPTIONS) as ydl:
            videos = ydl.extract_info(
                f"ytsearch{results_size}:{search_term}", download=False
            )["entries"]
            return jsonify(videos)
