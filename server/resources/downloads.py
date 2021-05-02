from flask import jsonify, Blueprint, request, send_file, Response

from utils.managers import session_manager


http = Blueprint(r"http_downloads", __name__)


@http.route("/downloads/<string:id>", methods=["GET", "POST", "DELETE"])
def download(id):
    session_id = request.args.get("sessionId")
    session_manager.update_session_use_time(session_id)
    download_manager = session_manager.get_download_manager(session_id)

    if request.method == "GET":
        path = download_manager.get_download(id)
        return send_file(path, as_attachment=True)
    elif request.method == "POST":
        url = request.json.get("url")
        download_manager.add(id, url)
        return jsonify({ "status": "ok" })
    elif request.method == "DELETE":
        download_manager.remove(id)
        return jsonify({ "status": "ok" })


@http.route("/downloads/status", methods=["GET"])
def downloads_status():
    session_id = request.args.get("sessionId")
    def status_stream():
        while True:
            msg = session_manager.get_status_queue(session_id).get()
            yield msg
    return Response(status_stream(), mimetype="text/event-stream")


