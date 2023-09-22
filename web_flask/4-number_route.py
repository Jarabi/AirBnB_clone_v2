#!/usr/bin/python3
""" A script that starts a Flask web application """
from flask import Flask
from markupsafe import escape

app = Flask(__name__)

# Disable strict slashes for all routes
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """ Displays: Hello HBNB! """
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """ Displays: HBNB """
    return "HBNB"


@app.route('/c/<text>')
def show_text(text):
    """
    Displays: C <text>
    Args:
        text: required string
    """

    # Replace underscores with spaces
    text = text.replace('_', ' ')

    return f"C {escape(text)}"


@app.route('/python/')
@app.route('/python/<text>')
def default_value(text="is cool"):
    """
    Displays: Python <text>
    Args:
        text: Optional, default value "is cool"
    """
    text = text.replace('_', ' ')

    return f"Python {escape(text)}"


@app.route('/number/<int:n>')
def integer_value(n):
    """
    Displays: <int:n> is a number>
    Args:
        n: must be integer value
    """
    return f"{n} is a number"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
