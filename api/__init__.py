from flask import Flask, app
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from api.Blog.blog_model import blogs
app.register_blueprint(blogs)

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://EntertainmentMp3.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    CORS(app)

    db.init_app(app)

    return app
