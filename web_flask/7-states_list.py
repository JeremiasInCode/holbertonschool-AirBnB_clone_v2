#!/usr/bin/python3
"""
Starts a Flask web application.

This module contains a Flask web application that displays a list of states.
"""
from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def statesList():
    """Displays an HTML page"""
    return render_template("7-states_list.html",
                           states=storage.all(State).values())


@app.teardown_appcontext
def tearDown(arg=None):
    """Ends the current session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
