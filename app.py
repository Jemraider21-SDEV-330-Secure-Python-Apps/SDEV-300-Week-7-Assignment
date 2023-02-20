"""Main application for the flask program
"""
from datetime import datetime
from flask import Flask
from flask import render_template
from flask import request
from functionality.lab2_functionality import generate_password

from models.lab1_model import Lab1Model

app: Flask = Flask(__name__)


@app.route("/")
def index() -> str:
    """Displaying the home page

    Returns:
        str: The home webpage
    """
    return render("index.html")


@app.route("/lab1/", methods=["GET", "POST"])
def lab1() -> str:
    """Routing for voter registration portion of lab1

    Returns:
        str: webpage for voter registration
    """
    if request.method == "GET":
        return render("lab1/lab1_form.html")
    if request.method == "POST":
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        model = Lab1Model(f'{fname} {lname}',
                          request.form.get("age"),
                          request.form.get("state"),
                          request.form.get("zipcode"))
        return render("lab1/lab1_result.html", model)


@app.route("/lab2/password/", methods=["GET", "POST"])
def lab2_password() -> str:
    """Routing for password generation section of lab2

    Returns:
        str: webpages for password generation
    """
    if request.method == "GET":
        return render("lab2/password/lab2_password_form.html")
    if request.method == "POST":
        password: str = generate_password(request.form)
        return render("lab2/password/lab2_password_result.html", password)


def render(file: str, data=False) -> str:
    """Calling the render_template function with other additions

    Args:
        file (str): html file for the webpage
        ex: index.html

    Returns:
        str: the webpage for the file
    """
    date_str: str = str(datetime.now().strftime("%a, %b %-d, %Y"))
    if data is False:
        return render_template(file, date=date_str)
    return render_template(file, data=data, date=date_str)
