#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """desplay hello hbnb"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def _hbnb():
    """display hbnb"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """display c followed by the value of the text variable"""
    text_replaced = text.replace('_', ' ')
    return "C {}".format(text_replaced)


@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text):
    """display python followed by the value of the text variable"""
    text_replaced = text.replace('_', ' ')
    return "Python {}".format(text_replaced)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """display n  if n is an integer"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number__template(n):
    """display  a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>")
def number_odd_or_even(n):
    """display if n even or odd"""
    if n % 2 == 0:
        even_odd = "even"
    else:
        even_odd = "odd"
    return render_template('6-number_odd_or_even.html',
                           n=n, even_odd=even_odd)


if __name__ == "__main__":
    """start flask and listen 0.0.0.0, port 5000"""
    app.run(host='0.0.0.0', port=5000)
