from flask import Flask, request, redirect, url_for, render_template, flash, jsonify

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html.j2")

@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/about")
def about():
    return render_template("about.html.j2")

@app.route("/contact")
def contact():
    return render_template("contact.html.j2")

@app.route("/createname")
def create_name():
    return render_template("create_name.html.j2")

@app.route("/addname", methods=["POST"])
def addname():
    return render_template("index.html.j2",
                    firstname=request.form['firstname'],
                    lastname=request.form['lastname'])

if __name__ == '__main__':
    app.run(debug=True)
