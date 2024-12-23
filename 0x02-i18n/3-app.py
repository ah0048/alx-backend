#!/usr/bin/env python3
""" Basic Flask app, Basic Babel setup
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """ Config class for Babel
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel()
babel.init_app(app)


@babel.localeselector
def get_locale() -> str:
    """ get locale
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """ return index page
    """
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
