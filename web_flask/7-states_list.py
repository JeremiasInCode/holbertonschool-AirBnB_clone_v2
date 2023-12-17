#!/usr/bin/python3

""" script that starts a Flask web application
    defines routes to handle specific urls
    fetching data from the storage engine
"""

from flask import Flask
from flask import render_template
import models
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states_list")
def states_list():
    """Returns a state list of elements"""
    d_states = models.storage.all(State)
    return render_template("7-states_list.html", stateslist=d_states.values())


@app.teardown_appcontext
def teardown(self):
    """close of storage of all models"""
    models.storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
