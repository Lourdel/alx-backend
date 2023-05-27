#!/usr/bin/env python3
"""Module implements basic Flask app"""

from flask import Flask, render_template, request
from flask_babel import Babel, gettext
from datetime import datetime

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """class configures languages"""
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"
    LANGUAGES = ["en", "fr"]


app.config.from_object(Config)


@app.route("/", strict_slashes=False)
def index():
    """renders 4-index.html"""
    return render_template("4-index.html")


#@babel.localeselector
def get_locale():
    """method gets the location"""
    local = request.args.get("locale")
    if local and local in app.config["LANGUAGES"]:
        return local
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
