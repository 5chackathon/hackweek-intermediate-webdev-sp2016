import os

from flask import render_template, request
from yelpapi import YelpAPI

from chirp import app

yelp_api = YelpAPI(os.environ['YELP_KEY'], os.environ['YELP_SECRET'],
                   os.environ['YELP_TOKEN'], os.environ['YELP_TOKEN_SECRET'])

@app.route("/")
def index():
    try:
        yelp_rs = yelp_api.search_query(location=request.args.get("location"))
    return render_template("index.html", name="Ross")

@app.route("/search")
def search():
    return request.args.get("location")
