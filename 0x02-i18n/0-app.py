#!/usr/bin/env python3
""" Simple flask app """

from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET'], strict_slashes=False)
def hello_world() -> str:
    """Basic Template for Babel Implementation"""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
