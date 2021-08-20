# Dependencies
# we'll use Flask to render a template, redirecting to another url, and creating a URL
from flask import Flask, render_template, redirect, url_for
# Use PyMongo to interact with our Mongo database
from flask_pymongo import PyMongo
# To use the scraping code, we will convert from Jupyter notebook to Python
import scraping

# -------------
# Set up flask
app = Flask(__name__)

# Tell Python how to connect to Mongo using PyMongo
# Use flask_pymongo to set up mongo connection
# Our app will connect to Mongo using a URI, a uniform resource identifier similar to a URL
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Defining routes
@app.route("/")
def index():
    # uses PyMongo to find the "mars" collection in our database
   mars = mongo.db.mars.find_one()
   # tells Flask to return an HTML template using an index.html file
   return render_template("index.html", mars=mars)

# Scrap
@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update({}, mars_data, upsert=True)
   return redirect('/', code=302)