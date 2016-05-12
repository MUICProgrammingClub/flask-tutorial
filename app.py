from flask import Flask, request, redirect, url_for, render_template, flash, jsonify
from helpers import header_active
import random
import datetime

app = Flask(__name__)

restaurants = open("restaurants", "r")
arr = restaurants.readlines()

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html.j2",
                            current_page="home",
                            header_active=header_active)

@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/about")
def about():
    return render_template("about.html.j2",
                            current_page="about",
                            header_active=header_active,
                            title="About")

@app.route("/contact")
def contact():
    return render_template("contact.html.j2",
                            current_page="contact",
                            header_active=header_active,
                            title="Contact")

@app.route("/addname")
def add_name():
    return render_template("addname.html.j2",
                            current_page="addname",
                            header_active=header_active,
                            title="Add name")

@app.route("/create", methods=["POST"])
def create_name():
    fullname = request.form['firstname'] + request.form['lastname']
    if len(fullname) == 0:
        return redirect(url_for('add_name'))
    return render_template("index.html.j2",
                    firstname=request.form['firstname'],
                    lastname=request.form['lastname'],
                    current_page="home",
                    header_active=header_active)

@app.route('/random')
def random_restaurant():
    restaurant = random.choice(arr)
    now = datetime.datetime.now().ctime()
    return render_template("random.html.j2",
                            restaurant=restaurant,
                            header_active=header_active,
                            now=now,
                            title="Random Restaurants")

@app.route('/random_extra')
def random_extra():
    all_restaurant = arr
    return render_template("random_extra.html.j2",
                            header_active=header_active,
                            all_restaurant = all_restaurant)

if __name__ == '__main__':
    app.run(debug=True)
