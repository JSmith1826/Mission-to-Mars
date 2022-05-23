# Import dependencies
from flask import Flask, render_template, redirect, url_for
from flask_pymongo import flask_pymongo
import scraping

# create app variable / set up Flask
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_db"
mongo = Pymongo(app)

@app.route("/")
def index:
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

    @app.route("/scrape")
    def scrape():
        mars = mongo.db.marsmars_data = scraping.scrape_all
        mars.update_one({}, {"$set":mars_data}, upsert=True)
        return redirect('/', code=302)

    if __name__ == "__main__":
        app.run()