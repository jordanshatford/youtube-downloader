import uuid

from flask import jsonify, Blueprint


http = Blueprint(r"http_session", __name__)


@http.route("/session", methods=["GET"])
def get_session():
    return jsonify({"sessionId": uuid.uuid4()})
