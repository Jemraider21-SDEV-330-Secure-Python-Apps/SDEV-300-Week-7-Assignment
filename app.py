"""Main application for the flask program
"""
from datetime import datetime
from flask import Flask
from flask import render_template
from flask import request

app: Flask = Flask(__name__)


@app.route("/")
def index() -> str:
    """Displaying the home page

    Returns:
        str: The home webpage
    """
    return render("index.html")


@app.route("/lab1/", methods=["GET", "POST"])
def lab1():
    if request.method == "GET":
        return render("lab1/lab1_form.html")

def render(file: str) -> str:
    """Calling the render_template function with other additions

    Args:
        file (str): html file for the webpage
        ex: index.html

    Returns:
        str: the webpage for the file
    """
    date_str: str = str(datetime.now().strftime("%a, %b %-d, %Y"))
    return render_template(file, date=date_str)
