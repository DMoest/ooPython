#!/usr/bin/env python3
from app import app
from flask import render_template

@app.route("/")
@app.route("/index")
def index():
    """
    Index route function.
    """
    return render_template("index.html")


@app.route("/yatzy")
def yatzy():
    """
    Yatzy route function.
    """
    return render_template("yatzy.html")


@app.errorhandler(404)
def page_not_found(e):
    """
    Handler for page not found 404
    """
    #pylint: disable=unused-argument
    return "Flask 404 here, but not the page you requested."


@app.errorhandler(500)
def internal_server_error(e):
    """
    Handler for internal server error 500
    """
    #pylint: disable=unused-argument
    return "<p>Flask 500<pre>" + traceback.format_exc()
