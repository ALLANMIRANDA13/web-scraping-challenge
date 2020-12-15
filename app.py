from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)
app.config["MONGO_ALLAN"] = "mongodb://localhost:27017/mars"
mongo = PyMongo(app)

# Create a root route / that will query your Mongo database and pass 
# the mars data into an HTML template to display the data.

@app.route("/")
def index():
    
    mars_page = mongo.db.pages.find_one()
    return render_template("index.html", mars_page=mars_page)

# create a route called /scrape that will import your scrape_mars.py 
# script and call your scrape function.

@app.route("/scrape")
def scraper():
    
    pages = mongo.db.pages
    mars_data = scrape_mars.scrape()
    pages.update({}, mars_data, upsert=True)
    return redirect("/", code=302)
    
if __name__ == "__main__":
    app.run(debug=True)

