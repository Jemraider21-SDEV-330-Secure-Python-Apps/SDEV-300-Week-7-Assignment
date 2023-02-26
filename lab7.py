"""Main application for the flask program
"""
from datetime import datetime
import string
from flask import Flask
from flask import render_template
from flask import request
from flask import flash
from passlib.hash import sha256_crypt

from models.lab1_model import Lab1Model
from models.lab2_password_model import Lab2PasswordModel
from models.lab2_percentage_model import Lab2PercentageModel
app: Flask = Flask(__name__)
app.secret_key = "We hide things in the places we know"


@app.route("/")
def index() -> str:
    """Displaying the home page

    Returns:
        str: The home webpage
    """
    return render("index.html")


@app.route("/registration", methods=["GET", "POST"])
def registration() -> str:
    """Display the registration form webpage

    Returns:
        str: webpage for registration form
    """
    if request.method == "POST":
        username: str = request.form.get("username")
        password: str = request.form.get("password")
        if len(password) < 12:
            flash("Password is less than 8 characters.")
            return render("user_auth/registration/registration_form.html")
        error_msgs: list[str] = []
        has_lower = password_validation(
            password, string.ascii_lowercase, "Password does not contain a lower case letter")
        if has_lower[0] is False:
            error_msgs.append(has_lower[1])

        has_upper = password_validation(
            password, string.ascii_uppercase, "Password does not contain an upper case letter")
        if has_upper[0] is False:
            error_msgs.append(has_upper[1])

        has_number = password_validation(
            password, string.digits, "Password does not contain a number")
        if has_number[0] is False:
            error_msgs.append(has_number[1])

        has_special: bool = password_validation(
            password, string.punctuation, "Password does not contain a special character")
        if has_special[0] is False:
            error_msgs.append(has_special[1])

        if len(error_msgs) != 0:
            for error_msg in error_msgs:
                flash(error_msg)
            return render("user_auth/registration/registration_form.html")

        password = sha256_crypt.hash(password)
        with open("user_info/users.txt", "a", encoding="UTF-8") as file:
            file.write(f'{username} {password}\n')
        flash("You have successfully registered")
        return render("index.html")
    return render("user_auth/registration/registration_form.html")


def password_validation(password: str, char_set, error_msg: str) -> list[bool, str]:
    """Validating a provided password for a specific requirement

    Args:
        password (str): user provided password
        char_set (_type_): set of characters to check if password contains
        error_msg (str): error message for validation

    Returns:
        list[bool, str]:
            bool: whether the password is valid
            str: error message if not valid
    """
    result: list[bool, str] = []
    found: bool = False
    for char in char_set:
        if password.find(char) != -1:
            found = True
            break
    result.append(found)
    if found is False:
        result.append(error_msg)
    return result


@app.route("/login", methods=["GET", "POST"])
def login() -> str:
    """Routing for login information

    Returns:
        str: webpage for login
    """
    if request.method == "POST":
        username: str = request.form.get("username")
        password: str = request.form.get("password")
        found_user: bool = False
        correct_password: bool = False
        error_msg: str = "Username was not correct."
        with open("user_info/users.txt", "r", encoding="UTF-8") as file:
            for line in file.readlines():
                information: list[str] = line.split(" ")
                if username == information[0]:
                    found_user = True
                    error_msg = "Password was not correct."
                    if sha256_crypt.verify(password, information[1]):
                        correct_password = True
                        error_msg = ""
                    break
        print("Found User: ", found_user)
        print("Correct password: ", correct_password)
        print(error_msg)
        correct_info: bool = all([found_user, correct_password])
        print("Result: ", correct_info)
        if correct_info is False:
            flash(error_msg)
            return render("user_auth/login/login_form.html")
        flash("You were successfully logged in")
        return render("index.html")
    return render("user_auth/login/login_form.html")


@app.route("/lab1/", methods=["GET", "POST"])
def lab1() -> str:
    """Routing for voter registration portion of lab1

    Returns:
        str: webpage for voter registration
    """
    if request.method == "POST":
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        model = Lab1Model(f'{fname} {lname}',
                          request.form.get("age"),
                          request.form.get("state"),
                          request.form.get("zipcode"))
        return render("lab1/lab1_result.html", model)

    # Assume a GET request
    return render("lab1/lab1_form.html")


@app.route("/lab2/password/", methods=["GET", "POST"])
def lab2_password() -> str:
    """Routing for password generation section of lab2

    Returns:
        str: webpages for password generation
    """
    if request.method == "POST":
        form = request.form
        print(form)
        model = Lab2PasswordModel(
            length=int(form.get("length")),
            lowercase=bool(form.get("lowercase")),
            uppercase=bool(form.get("uppercase")),
            numbers=bool(form.get("numbers")),
            specials=bool(form.get("specials")))
        password: str = model.generate()
        return render("lab2/password/lab2_password_result.html", password)

    # Assume a GET request
    return render("lab2/password/lab2_password_form.html")


@app.route("/lab2/percentage/", methods=["GET", "POST"])
def lab2_percentage() -> str:
    """Routing for Lab 2 Percentage

    Returns:
        str: Webpage for Lab 2 Percentage
    """
    if request.method == "POST":
        form = request.form
        model = Lab2PercentageModel(float(form.get("numerator")),
                                    float(form.get("denominator")),
                                    int(form.get("decimals")))
        return render("lab2/percentage/lab2_percentage_result.html", model)

    # Assume a GET request
    return render("lab2/percentage/lab2_percentage_form.html")


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
