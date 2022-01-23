#!/usr/bin/env python3

# Module imports
from flask_assets import Environment, Bundle
from flask import Flask

# Config Application & Assets
app = Flask(__name__)
assets = Environment(app)

# Bundle Flask Assets
style = Bundle('styles/**/*.css', 'styles/**/*.scss', output='dist/main.css', filters='postcss')
# js = Bundle("js/**/*.js", "./**/*.js", output="dist/bundle.js")

# Register Bundled Assets for useage
assets.register('style', style)
# assets.register("js", js)

# Build Flask Assets
# style.build()
# js.build()

from router import routes

if __name__ == "__main__":
    app.run()
