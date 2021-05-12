from flask import jsonify, Blueprint, request

from utils.youtube import search_youtube


http = Blueprint(r"http_search", __name__)


@http.route("/search", methods=["GET"])
def search():
    term = request.args.get("term")
    results_size = request.args.get("results", 6)
    return jsonify(search_youtube(term, results_size)), 200
