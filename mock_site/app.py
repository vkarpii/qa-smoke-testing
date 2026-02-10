"""
Mock web application module.

This module defines a simple Flask web application used as a target
for smoke automation testing. The application provides:
    - Basic navigation pages
    - A deliberately broken endpoint for negative testing
    - Custom error handling

The app is configured via an external JSON configuration file.
"""

import json

from flask import Flask, render_template, abort

app = Flask(__name__)
with open("config/config.json") as f:
    config = json.load(f)

@app.route("/")
def home():
    """
    Home page endpoint.
    """
    return render_template("components/home-content.html")

@app.route("/about")
def about():
    """
    About page endpoint.
    """
    return render_template("components/about-content.html")

@app.route("/broken")
def broken():
    """
    Broken endpoint for negative testing.
    """
    abort(404)

@app.errorhandler(404)  
def page_not_found(e):
    '''
    Custom 404 error handler.
    '''
    return render_template("components/page-not-found.html"), 404

app.run(port = config["port"], debug= config["debug"])