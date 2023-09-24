#!/usr/bin/python3
""" A script that starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

# Disable strict slashes for all routes
app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def cities_by_states():
    """ Get all states """
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def tear_down(arg=None):
    """ Remove SQLAlchemy session """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
