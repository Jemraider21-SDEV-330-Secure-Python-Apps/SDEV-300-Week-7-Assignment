import string
import random
from werkzeug.datastructures import ImmutableMultiDict
from models.lab2_password_model import Lab2PasswordModel


def generate_password(form: ImmutableMultiDict[str, str]
                      ) -> str:
    """Generate a secure password based on user input

    Args:
        form (ImmutableMultiDict[str, str]): The data structure for the user input from the form

    Returns:
        str: generated password
    """
    input = Lab2PasswordModel(int(form.get("length")),
                              bool(form.get("lowercase")),
                              bool(form.get("uppercase")),
                              bool(form.get("numbers")),
                              bool(form.get("specials")))
    characters: str = ""
    all_false_input = not any(
        [input.lowercase, input.uppercase, input.numbers, input.specials])
    if all_false_input:
        characters = string.ascii_letters
    else:
        characters = adding_characters(
            characters, input.lowercase, string.ascii_lowercase)
        characters = adding_characters(
            characters, input.uppercase, string.ascii_uppercase)
        characters = adding_characters(
            characters, input.numbers, string.digits)
        characters = adding_characters(
            characters, input.specials, string.punctuation)
    password: str = "".join(random.choice(characters)
                            for i in range(input.length))
    return password


def adding_characters(characters: str, to_use: bool, to_add: str) -> str:
    """Concatenates a new string to an existing set of characters if the user selects to use them
    Args:
        characters (str): The base set of characters to use
        to_use (bool): User selection for whether to join the two strings together
        to_add (str): the characters to add to the original set of characters
    Returns:
        str: The set of valid characters to use when creating a password
    """
    return characters + to_add if to_use else characters
