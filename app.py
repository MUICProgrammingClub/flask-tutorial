from flask import Flask, request, redirect, url_for, render_template, flash, jsonify
from helpers import header_active

app = Flask(__name__)

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
                            header_active=header_active)

@app.route("/contact")
def contact():
    return render_template("contact.html.j2",
                            current_page="contact",
                            header_active=header_active)

@app.route("/addname")
def add_name():
    return render_template("addname.html.j2",
                            current_page="addname",
                            header_active=header_active)

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

if __name__ == '__main__':
    app.run(debug=True)
