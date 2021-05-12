import uuid

from flask import jsonify, Blueprint

from utils.managers import session_manager


http = Blueprint(r"http_session", __name__)


@http.route("/session", methods=["GET"])
def get_session():
    session_id = str(uuid.uuid4())
    session_manager.setup_session(session_id)
    return jsonify({"sessionId": session_id}), 200
