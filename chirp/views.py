import os

from flask import render_template, request, redirect, url_for
from yelpapi import YelpAPI
from firebase import firebase

from chirp import app

yelp_api = YelpAPI(os.environ['YELP_KEY'], os.environ['YELP_SECRET'],
                   os.environ['YELP_TOKEN'], os.environ['YELP_TOKEN_SECRET'])

firebase = firebase.FirebaseApplication('https://yelphackweek.firebaseio.com/', None)

@app.route("/")
def index():
    return render_template("index.html", search_page = True)

@app.route("/search")
def search():
    try:
        yelp_rs = yelp_api.search_query(location=request.args.get("location"))

        businesses = [{"image_url": i['image_url'][:-6] + 'ls.jpg', "name": i["name"], "description" : i["snippet_text"], "rating" : i["rating_img_url"], "id" : i["id"]}
                  for i in yelp_rs['businesses']]
    except (YelpAPI.YelpAPIError):
        return "Oops! Error!"
    return render_template("index.html", businesses=businesses, search_page = True)

@app.route("/save")
def save():
    try:
        business_id = request.args.get("id")
        business_rs = yelp_api.business_query(id=business_id)
        result = firebase.post('/Restaurants', {
            "image_url" : business_rs["image_url"][:-6] + "ls.jpg",
            "name" : business_rs["name"],
            "description" : business_rs["snippet_text"],
            "rating" : business_rs["rating_img_url"],
            "id" : business_rs["id"]
        })
        return redirect(url_for("favorites"))
    except (YelpAPI.YelpAPIError):
        return "Error!"

@app.route("/favorites")
def favorites():
    restaurants = firebase.get("/Restaurants", None)
    businesses = []
    for k in restaurants:
        businesses.append(restaurants[k])
    return render_template("index.html", businesses=businesses, search_page = False)
