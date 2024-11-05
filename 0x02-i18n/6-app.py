#!/usr/bin/env python3
""" Basic Flask app, Basic Babel setup
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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


def get_user():
    """ get user
    """
    try:
        return users.get(int(request.args.get('login_as')))
    except Exception:
        return None


@app.before_request
def before_request():
    """ before request
    """
    user = get_user()
    if user:
        g.user = user
    else:
        g.user = None


@babel.localeselector
def get_locale() -> str:
    """ get locale
    """
    # Check for locale from URL parameters
    language = request.args.get('locale')
    if language and language in app.config['LANGUAGES']:
        return language

    # Check for locale from user settings
    if g.user:
        user_language = g.user.get('locale')
        if user_language and user_language in app.config['LANGUAGES']:
            return user_language

    # Check for locale from request headers
    language = request.accept_languages.best_match(app.config['LANGUAGES'])
    if language:
        return language

    # Default locale
    return app.config['BABEL_DEFAULT_LOCALE']


@app.route('/', strict_slashes=False)
def index() -> str:
    """ return index page
    """
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
