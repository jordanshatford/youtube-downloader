from flask import Flask, send_from_directory
from flask import jsonify
import random

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# Path for our main Svelte page
@app.route("/")
def base():
    return send_from_directory('../client/public', 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('../client/public', path)


@app.route("/rand")
def hello():
    return str(random.randint(0, 100))
