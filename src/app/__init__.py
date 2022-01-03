import click
from flask import Flask
from flask.cli import FlaskGroup
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
from flask import Blueprint

db = SQLAlchemy()

bp = Blueprint('blog', __name__)


@bp.cli.command('create')
def create_app(create):
    app = Flask('create')
    app.config.from_object(Config)
    db.init_app(app)
    app.register_blueprint(bp)
    return app


@click.group(cls=FlaskGroup, create_app=create_app)
def cli():
    """Koose is Here"""
