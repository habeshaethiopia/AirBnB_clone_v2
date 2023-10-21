#!/usr/bin/python3
"""the flask app"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def C(text):
    return "C " + text.replace("_", " ")


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python", strict_slashes=False)
def python(text="is cool"):
    return "Python " + text.replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def num(n):
    return("{} is a number".format(n))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
