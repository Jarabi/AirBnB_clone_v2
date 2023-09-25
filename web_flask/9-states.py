#!/usr/bin/python3
""" A script that starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

# Disable strict slashes for all routes
app.url_map.strict_slashes = False


@app.route('/states')
def get_states():
    """ Get all the states """
    states = storage.all(State)

    return render_template('9-states.html', states=states)


@app.route('/states/<id>')
def get_state(id):
    """
    Get state

    Args:
        id: alpha-numeric state id
    """
    states = storage.all(State)

    for state in states.values():
        if state.id == id:
            return render_template('9-states.html', state=state)

    return render_template('9-states.html', state='Not Found!')


@app.teardown_appcontext
def tear_down(arg=None):
    """ Remove SQLAlchemy session """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
