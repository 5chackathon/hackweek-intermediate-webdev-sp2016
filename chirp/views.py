import os

from flask import render_template, request
from yelpapi import YelpAPI

from chirp import app

yelp_api = YelpAPI(os.environ['YELP_KEY'], os.environ['YELP_SECRET'],
                   os.environ['YELP_TOKEN'], os.environ['YELP_TOKEN_SECRET'])

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():
    try:
        yelp_rs = yelp_api.search_query(location=request.args.get("location"))
        yelp_bs = yelp_rs["businesses"]

        businesses = []
        for b in yelp_bs:
            businesses.append(b["image_url"])
        # businesses = [{"image_url": i['image_url'][:-6] + 'ls.jpg', "busid": i["id"]}
        #           for i in yelp_rs['businesses']]

    except (YelpAPI.YelpAPIError):
        return "Oops! Error!"
    return render_template("index.html", businesses=businesses)
