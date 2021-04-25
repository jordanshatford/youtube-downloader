from flask import Flask
from flask_cors import CORS
from flask_sockets import Sockets

from resources.search import http as HttpSearchEndpoints
from resources.session import http as HttpSessionEndpoints
from resources.session import ws as WsSessionEndpoints

app = Flask(__name__)
sockets = Sockets(app)
CORS(app, supports_credentials=True)

app.register_blueprint(HttpSearchEndpoints, url_prefix="/api")
app.register_blueprint(HttpSessionEndpoints, url_prefix="/api")
sockets.register_blueprint(WsSessionEndpoints, url_prefix="/ws")

from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer

http_server = WSGIServer(('',8000), app, handler_class=WebSocketHandler)
http_server.serve_forever()