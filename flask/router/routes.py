#!/usr/bin/env python3
from app import app
from flask import render_template
from src.hand import Hand

routes = [
    {'name': 'Index', 'route': '/index'},
    {'name': 'Yatzy', 'route': '/yatzy'},
    {'name': 'About', 'route': '/about'}
]


@app.route("/")
@app.route("/index")
def index():
    """
    Index route function.
    """
    return render_template("views/index.html", title="Välkommen!", pages=routes)


@app.route("/yatzy")
def yatzy():
    """
    Yatzy route function.
    """
    hand = Hand()
    hand.roll()

    return render_template("views/yatzy.html", title="Yatzy", pages=routes, hand=hand)


@app.route("/about")
def about():
    """
    Aboute route
    """
    return render_template("views/about.html", title="Om mig", pages=routes)


@app.errorhandler(404)
def page_not_found(e):
    """
    Handler for page not found 404
    """
    # pylint: disable=unused-argument
    return "Flask 404 here, but not the page you requested."


@app.errorhandler(500)
def internal_server_error(e):
    """
    Handler for internal server error 500
    """
    # pylint: disable=unused-argument
    return "<p>Flask 500<pre>" + traceback.format_exc()
