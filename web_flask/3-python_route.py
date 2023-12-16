#!/usr/bin/python3
"""Starts a Flask web app"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """ Displays 'Hello HBNB!' """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Displays 'HBNB!' """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_text(text):
    """ Displays 'C' <text> """
    text_replaced = text.replace("_", " ")
    return "C " + text_replaced


@app.route("/python")
@app.route("/python/<text>")
def display_text(text="is cool"):
    """ Returns a text """
    text = text.replace("_", " ")
    return "Python " + text


if __name__ == "__main__":
    app.run(host="0.0.0.0")
