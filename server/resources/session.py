import uuid
import os

from flask import jsonify, Blueprint
from geventwebsocket.exceptions import WebSocketError

http = Blueprint(r"http_session", __name__)
ws = Blueprint(r"ws_session", __name__)

@http.route("/session", methods=["GET"])
def get_session():
    return jsonify({"sessionId": uuid.uuid4()})

@ws.route("/session")
def session_socket(websocket):
    sessionId = None
    while not websocket.closed:
        try:
            message = websocket.receive()
            if message is not None:
                sessionId = str(message)
                path = get_path_to_session_files(sessionId)
                if not os.path.exists(path):
                    os.mkdir(path)
            websocket.send(message)
        except WebSocketError as e:
            print("Connection closed. Message: " + e.__class__.__name__ + ": " + str(e))
            print(sessionId)
            path = get_path_to_session_files(sessionId)
            if os.path.exists(path):
                os.rmdir(path)
            break
    print("Connection closed. Message: ")
    print(sessionId)


def get_path_to_session_files(sessionId):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return f"{dir_path}/sessions/{sessionId}"