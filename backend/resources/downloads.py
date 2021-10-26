import os

from flask import jsonify, Blueprint, request, send_file, Response

from utils.helpers import format_response_message
from utils.managers import session_manager


http = Blueprint(r"http_downloads", __name__)


@http.route("/downloads/<string:id>", methods=["GET", "POST", "DELETE"])
def download(id: str):
    session_id = request.args.get("sessionId")
    session_manager.update_session_use_time(session_id)
    download_manager = session_manager.get_download_manager(session_id)

    if request.method == "GET":
        path = download_manager.get_download(id)
        if path is not None and os.path.exists(path):
            return send_file(path, as_attachment=True)
        else:
            return jsonify(
                format_response_message(
                    message="File Missing",
                    detail="The file was not found on the server. Try downloading again.",
                )
            ), 500
    elif request.method == "POST":
        url = request.json.get("url")
        download_manager.add(id, url)
        return jsonify(
            format_response_message(
                message="File Added",
                detail="The requested file has been successfully added to download.",
            )
        ), 200
    elif request.method == "DELETE":
        download_manager.remove(id)
        return jsonify(
            format_response_message(
                message="File Removed",
                detail="The requested file has been removed from the server.",
            )
        ), 200


@http.route("/downloads/status", methods=["GET"])
def downloads_status():
    session_id = request.args.get("sessionId")

    def status_stream():
        while True:
            msg = session_manager.get_status_queue(session_id).get()
            yield msg

    return Response(status_stream(), mimetype="text/event-stream")
