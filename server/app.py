import atexit
import os
import shutil

from flask import Flask
from flask_cors import CORS
from waitress import serve

from resources.downloads import http as HttpDownloadsEndpoints
from resources.search import http as HttpSearchEndpoints
from resources.session import http as HttpSessionEndpoints
from utils.managers import session_manager


@atexit.register
def shutdown_cleanup():
    # Remove all session files
    if os.path.exists(session_manager.session_dir):
        shutil.rmtree(session_manager.session_dir)


API_PREFIX = "/api"
app = Flask(__name__)
CORS(app)

app.register_blueprint(HttpDownloadsEndpoints, url_prefix=API_PREFIX)
app.register_blueprint(HttpSearchEndpoints, url_prefix=API_PREFIX)
app.register_blueprint(HttpSessionEndpoints, url_prefix=API_PREFIX)

if __name__ == "__main__":
    host = os.environ.get("HOST", "0.0.0.0")
    port = int(os.environ.get("PORT", 8080))
    threads = int(os.environ.get("WAITRESS_THREADS", 4))
    print(f"Serving on {host}:{port} with {threads} threads.", flush=True)
    serve(app, host=host, port=port, threads=threads)
