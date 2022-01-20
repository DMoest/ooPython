#!/usr/bin/env python3

# Module imports
from flask import Flask

app = Flask(__name__)

from router import routes

if __name__ == "__main__":
    app.debug = True
    app.run()
