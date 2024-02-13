#!/usr/bin/env python3
"""
Flask app that uses babel
"""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """
    Babels config class
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route("/")
def index():
    """Render index page here"""
    return render_template("1-  index.html")


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
