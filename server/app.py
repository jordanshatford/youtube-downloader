import atexit
import os
import shutil

from flask import Flask
from flask_cors import CORS

from resources.downloads import http as HttpDownloadsEndpoints
from resources.search import http as HttpSearchEndpoints
from resources.session import http as HttpSessionEndpoints
from utils.managers import session_manager


@atexit.register
def shutdown_cleanup():
    # Remove all session files
    if os.path.exists(session_manager.session_dir):
        shutil.rmtree(session_manager.session_dir)


def create_app():
    API_PREFIX = "/api"
    app = Flask(__name__)
    CORS(app)

    app.register_blueprint(HttpDownloadsEndpoints, url_prefix=API_PREFIX)
    app.register_blueprint(HttpSearchEndpoints, url_prefix=API_PREFIX)
    app.register_blueprint(HttpSessionEndpoints, url_prefix=API_PREFIX)

    return app
