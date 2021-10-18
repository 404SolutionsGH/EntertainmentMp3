from flask import Flask
from flask_jwt_extended.jwt_manager import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import click
from flask.cli import with_appcontext
from werkzeug.security import generate_password_hash

from api.Blog.blog_model import blogs


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://EntertainmentMp3.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'kose060'
    CORS(app)
    jwt = JWTManager(app)
    db.init_app(app)
    app.register_blueprint(blogs)

    @click.command(name='create_admin')
    @with_appcontext
    def create_admin():
        admin = User(email="admin_email_address", password='admin_password')
        admin.password = generate_password_hash(
            admin.password, 'sha256', salt_length=12)
        db.session.add(admin)
        db.session.commit()

    app.cli.add_command(create_admin)

    return app
