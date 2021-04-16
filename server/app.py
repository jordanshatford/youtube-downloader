from flask import Flask, send_from_directory
from flask import jsonify
from flask import request
from youtube_dl import YoutubeDL

app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0

# Path for our main Svelte page
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def base(path):
    return send_from_directory("../client/public", "index.html")

# Paths for all the static files (compiled JS/CSS, etc.)
@app.route("/build/<path:path>")
def build(path):
    return send_from_directory("../client/public/build", path)

@app.route("/images/<path:path>")
def images(path):
    return send_from_directory("../client/public/images", path)

@app.route("/global.css")
def globalCss():
    return send_from_directory("../client/public", "global.css")

@app.route("/favicon.png")
def favicon():
    return send_from_directory("../client/public", "favicon.png")

# Path to search for youtube videos using key terms
@app.route("/api/search", methods=["GET"])
def search_video():
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