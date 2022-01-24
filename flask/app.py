#!/usr/bin/env python3

"""
Main application mobule App.py
"""

# Module imports
from flask import Flask, render_template
from src.hand import Hand
# from flask_assets import Environment, Bundle

# Config Application & Assets
app = Flask(__name__)
# assets = Environment(app)
# from router import routes

# Bundle Flask Assets
# style = Bundle('styles/**/*.css', 'styles/**/*.scss', output='dist/main.css', filters='postcss')
# js = Bundle("js/**/*.js", "./**/*.js", output="dist/bundle.js")

# Register Bundled Assets for useage
# assets.register('style', style)
# assets.register("js", js)

# Build Flask Assets
# style.build()
# js.build()


# Routes
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


@app.route("/main")
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
    # pylint: disable=no-member
    # pylint: disable=unused-argument
    # pylint: disable=undefined-variable
    return "Flask 404 here, but not the page you requested."


@app.errorhandler(500)
def internal_server_error(e):
    """
    Handler for internal server error 500
    """
    # pylint: disable=no-member
    # pylint: disable=unused-argument
    # pylint: disable=undefined-variable
    return "<p>Flask 500<pre>" + traceback.format_exc()



if __name__ == "__main__":
    app.run()
