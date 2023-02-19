"""Main application for the flask program
"""
from datetime import datetime
from flask import Flask
from flask import render_template

app: Flask = Flask(__name__)


@app.route("/")
def index() -> str:
    """Displaying the home page

    Returns:
        str: The home webpage
    """
    return render("index.html")


@app.route("/scarycode")
def scarycode() -> str:
    """Displaying the page for 'Scary Code'

    Returns:
        str: the scarycode webpage
    """
    return render("scarycode.html")


@app.route("/howtohelp")
def howtohelp() -> str:
    """Displaying the page for 'How To Help'

    Returns:
        str: the howtohelp webpage
    """
    return render("howtohelp.html")


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
