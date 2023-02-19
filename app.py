from flask import Flask
from flask import render_template

app: Flask = Flask(__name__)


@app.route("/")
def index():
    # return "Hello world!"
    return render_template("index.html")
