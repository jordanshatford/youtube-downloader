from flask import Flask
from flask_cors import CORS

from resources.downloads import http as HttpDownloadsEndpoints
from resources.search import http as HttpSearchEndpoints
from resources.session import http as HttpSessionEndpoints


app = Flask(__name__)
CORS(app)

app.register_blueprint(HttpDownloadsEndpoints, url_prefix="/api")
app.register_blueprint(HttpSearchEndpoints, url_prefix="/api")
app.register_blueprint(HttpSessionEndpoints, url_prefix="/api")
