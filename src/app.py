from flask import Flask, jsonify
from flask.signals import message_flashed
from flask_script import Manager
from flask_migrate import MigrateCommand

from app import create_app
from app.database.models import Post

app = create_app()

manager = Manager(app)


manager.add_command('db', MigrateCommand)


@app.route("/")
def home():
    resp = dict(status='success', message='Welcome to blog application')
    return jsonify(resp)


if __name__ == '__main__':
    manager.run()
