import os

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_restful import Api

from resources.search import Search

app = Flask(__name__)
Session(app)
CORS(app)
api = Api(app)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", os.urandom(12).hex())
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    "DATABASE_URL", "sqlite:///db.sqlite3"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SESSION_TYPE"] = "sqlalchemy"
db = SQLAlchemy(app)
app.config["SESSION_SQLALCHEMY"] = db

api.add_resource(Search, "/api/search")

