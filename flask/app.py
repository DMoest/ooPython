#!/usr/bin/env python3

"""
Main application mobule App.py
"""

# Module imports
import os
import re
from flask import Flask, render_template, session, request, redirect, url_for

from handler import Handler
from src.rules import (
    Ones,
    Twos,
    Threes,
    Fours,
    Fives,
    Sixes,
    ThreeOfAKind,
    FourOfAKind,
    FullHouse,
    SmallStraight,
    LargeStraight,
    Chance,
    Yahtzee
)

# from flask_assets import Environment, Bundle

# Config Application & Assets
app = Flask(__name__)
handler = Handler()

# Session secret key.
app.secret_key = re.sub(r"[^a-z\d]", "", os.path.realpath(__file__))
# print("Session Key: ", re.sub(r"[^a-z\d]", "", os.path.realpath(__file__)))

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
    {'name': 'Index', 'route': 'index'},
    {'name': 'Yatzy', 'route': 'yatzy'},
    {'name': 'About', 'route': 'about'}
]

rules = [
    Ones(),
    Twos(),
    Threes(),
    Fours(),
    Fives(),
    Sixes(),
    ThreeOfAKind(),
    FourOfAKind(),
    FullHouse(),
    SmallStraight(),
    LargeStraight(),
    Chance(),
    Yahtzee()
]


@app.route("/")
@app.route("/index")
def index():
    """
    Index route function.
    """
    return render_template("views/index.html",
                           title="Välkommen!",
                           pages=routes)


@app.route("/main", methods=["GET", "POST"])
@app.route("/yatzy", methods=["GET", "POST"])
def yatzy():
    """
    Yatzy route function.
    """
    hand = handler.hand
    roll_these_dice = []
    session["last_hand"] = session.get("dice_hand")

    for i in request.form.getlist('select_to_keep'):
        roll_these_dice.append(int(i))

    if len(roll_these_dice) > 0:
        session["dice_hand"] = handler.roll(roll_these_dice)
    else:
        session["dice_hand"] = handler.roll()

    return render_template("views/yatzy.html",
                           title="Yatzy",
                           pages=routes,
                           hand=hand,
                           rules=rules)


@app.route("/select_score", methods=["GET", "POST"])
def select_score():
    """
    Select score route
    """
    if request.method == "POST":
        # handler.read_session(session)
        handler.add_to_scoreboard(request.form)

    return redirect(url_for('yatzy'))

@app.route("/reset", methods=["POST"])
def reset():
    """
    Aboute route
    """
    session.clear()
    session['scoreboard'] = {}

    return redirect(url_for('yatzy'))


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
    return render_template("views/404.html"), 404


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
