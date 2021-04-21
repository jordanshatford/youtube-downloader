from flask import jsonify, Flask, send_from_directory, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_restful import Resource, Api
from youtube_dl import YoutubeDL

app = Flask(__name__)
api = Api(app, prefix="/api")
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
app.config["SECRET_KEY"] = "TODO_SECRET_KEY"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
app.config["SESSION_TYPE"] = "sqlalchemy"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
app.config["SESSION_SQLALCHEMY"] = db
Session(app)

# Path for our main Svelte pages
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def base(path):
    return send_from_directory("../client/public", "index.html")

# Paths for all the static files (compiled JS/CSS, etc.)
@app.route("/<string:folder>/<string:filename>")
def build(folder, filename):
    return send_from_directory(f"../client/public/{folder}", filename)

# Search api for finding youtube videos
class Search(Resource):
    def get(self):
        YDL_OPTIONS = {
            "noplaylist": True,
            "quiet": True,
        }
        DEFAULT_SEARCH_RESULT_SIZE = 3
        search_term = request.args.get("term")
        results_size = request.args.get("results", DEFAULT_SEARCH_RESULT_SIZE)
        with YoutubeDL(YDL_OPTIONS) as ydl:
            videos = ydl.extract_info(f"ytsearch{results_size}:{search_term}", download=False)["entries"]
            return jsonify(videos)

api.add_resource(Search, '/search')