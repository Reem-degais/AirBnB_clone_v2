#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """display hello hbnb"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def _hbnb():
    """display hbnb"""
    return "HBNB"


if __name__ == "__main__":
    """start flask and listen 0.0.0.0, port 5000"""
    app.run(host='0.0.0.0', port=5000)
