from flask import jsonify, request
from flask_restful import Resource
from youtube_dl import YoutubeDL


class Search(Resource):
    def get(self):
        YDL_OPTIONS = {
            "noplaylist": True,
            "quiet": True,
        }
        DEFAULT_SEARCH_RESULT_SIZE = 5
        search_term = request.args.get("term")
        results_size = request.args.get("results", DEFAULT_SEARCH_RESULT_SIZE)
        with YoutubeDL(YDL_OPTIONS) as ydl:
            videos = ydl.extract_info(
                f"ytsearch{results_size}:{search_term}", download=False
            )["entries"]
            return jsonify(videos)
