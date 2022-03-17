#!/usr/bin/env python3

"""
Main application mobule App.py
"""
import os
import re

from flask import Flask, render_template, session, request, redirect, url_for
from handler import Handler

# Config Application & Assets
app = Flask(__name__)
handler = Handler()

# Session secret key.
app.secret_key = re.sub(r"[^a-z\d]", "", os.path.realpath(__file__))
# print("Session Key: ", re.sub(r"[^a-z\d]", "", os.path.realpath(__file__)))

# Routes
routes = [
    {'name': 'Index', 'route': 'index'},
    {'name': 'Yatzy', 'route': 'yatzy'},
    {'name': 'About', 'route': 'about'}
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
    # Check for all needed sessions to exist or set them up
    if handler.check_sessions() is False:
        handler.setup_sessions(handler)

    counter = handler.read_session("counter")

    dice_indexes = []
    if request.method == "POST" and counter < 3:
        for index in request.form.getlist('select_to_roll'):
            dice_indexes.append(int(index))

        handler.write_session("roll_these_dice", dice_indexes)
        # print(f"Dice index from session: {handler.read_session('roll_these_dice')}")

        # Roll them dices
        handler.roll(handler.read_session('roll_these_dice'))

    return render_template("views/yatzy.html",
                           title="Yatzy",
                           pages=routes,
                           hand=handler.get_hand(),
                           rules=handler.get_rules(),
                           counter=handler.get_counter(),
                           dice_hand=handler.get_dice_hand(),
                           scoreboard=handler.get_scoreboard(),
                           total_score=handler.get_total_score(),
                           finished=handler.is_finished())


@app.route("/select_score", methods=["GET", "POST"])
def select_score():
    """
    Select score route
    """
    if request.method == "POST":
        scores = handler.add_to_scoreboard(request.form)
        handler.write_session('scoreboard', scores)
    return redirect(url_for('yatzy'))


@app.route("/reset", methods=["POST"])
def reset():
    """
    Aboute route
    """
    session.clear()
    handler.reset_game()

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
