from flask import Flask, render_template

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

if __name__ == '__main__':
    app.run(debug=True)
