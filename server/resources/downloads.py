import json
import queue

from flask import jsonify, Blueprint, request, send_file, Response
from utils.managers import AudioDownloadManager
from utils.sse import ServerSentEvent

http = Blueprint(r"http_downloads", __name__)


@http.route("/downloads/<string:id>", methods=["GET", "POST", "DELETE"])
def download(id):
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


queue = queue.Queue()

def send_event(status, video_id):
    msg = ServerSentEvent(data=json.dumps({"status": status.value, "id": video_id}))
    queue.put(msg.encode())

download_manager = AudioDownloadManager("sessionId", announcer=send_event)


@http.route("/downloads/status", methods=["GET"])
def downloads_status():
    def status_stream():
        while True:
            msg = queue.get()  # blocks until a new message arrives
            yield msg

    return Response(status_stream(), mimetype="text/event-stream")


