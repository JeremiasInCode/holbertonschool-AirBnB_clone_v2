#!/usr/bin/python3
"""Starts a Flask web app"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_world():
    """ Displays 'Hello HBNB!' """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """ Displays 'HBNB!' """
    return "HBNB"


@app.route("/c/<text>")
def display_text_c(text):
    """ Displays 'C' <text> """
    text_replaced = text.replace("_", " ")
    return "C " + text_replaced


@app.route("/python", defaults={'text': 'is_cool'})
@app.route("/python/<text>")
def display_text_python(text):
    """ Returns a text """
    text = text.replace("_", " ")
    return "Python " + text


if __name__ == "__main__":
    app.run(host="0.0.0.0")
