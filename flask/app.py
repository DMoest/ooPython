#!/usr/bin/env python3

# Module imports
from flask import Flask
from flask_assets import Environment, Bundle

app = Flask(__name__)

# Bundle Flask Assets
style = Bundle('styles/**/*.css', 'styles/**/*.scss', output='dist/main.css', filters='postcss')
# js = Bundle("js/**/*.js", "./**/*.js", output="dist/bundle.js")

# Config Assets
assets = Environment(app)
assets.init_app(app)

# Register Assets
assets.register('style', style)
# assets.register("js", js)

# Build Flask Assets
style.build()
# js.build()

from router import routes

if __name__ == "__main__":
    app.run()
