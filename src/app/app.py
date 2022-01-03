from flask import Flask, jsonify
from flask.signals import message_flashed

app = Flask(__name__)


@app.route("/")
def home():
    resp = dict(status='success', message='Welcome to blog application')
    return jsonify(resp)


app.run('localhost', '5000', debug=True)
