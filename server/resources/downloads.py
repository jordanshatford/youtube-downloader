import json
from flask import jsonify, Blueprint, request, send_file, Response
from utils.managers import AudioDownloadManager
from utils.sse import ServerSentEvent, MessageAnnouncer

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


# TODO: move this to session manager
status_updater = MessageAnnouncer()

def send_event(status, video_id):
    msg = ServerSentEvent(data=json.dumps({"status": status.value, "id": video_id}))
    status_updater.announce(msg=msg.encode())

download_manager = AudioDownloadManager("sessionId", announcer=send_event)


@http.route("/downloads/status", methods=["GET"])
def downloads_status():
    def stream():
        messages = status_updater.listen()  # returns a queue.Queue
        while True:
            msg = messages.get()  # blocks until a new message arrives
            yield msg

    return Response(stream(), mimetype="text/event-stream")


