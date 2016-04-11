import os

from flask import render_template, request
from yelpapi import YelpAPI

from chirp import app


@app.route("/")
def index():
    return "Hello, 5CHackathon!"