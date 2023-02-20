from dataclasses import dataclass
import random
import string


class Lab2PasswordModel:
    """Model for generating secure password
    """
    length: int = 0
    lowercase: bool
    uppercase: bool
    numbers: bool
    specials: bool

    def __init__(self, length: int, lowercase: bool, uppercase: bool, numbers: bool, specials: bool) -> None:
        self.length: int = length
        self.lowercase: bool = lowercase
        self.uppercase: bool = uppercase
        self.numbers: bool = numbers
        self.specials: bool = specials

    def generate(self) -> str:
        """Generate a secure password based on user input

        Args:
            form (ImmutableMultiDict[str, str]): The data structure for the user input from the form

        Returns:
            str: generated password
        """
        characters: str = ""
        all_false_input = not any(
            [self.lowercase, self.uppercase, self.numbers, self.specials])
        if all_false_input:
            characters = string.ascii_letters
        else:
            characters = self.adding_characters(
                characters, self.lowercase, string.ascii_lowercase)
            characters = self.adding_characters(
                characters, self.uppercase, string.ascii_uppercase)
            characters = self.adding_characters(
                characters, self.numbers, string.digits)
            characters = self.adding_characters(
                characters, self.specials, string.punctuation)
        password: str = "".join(random.choice(characters)
                                for i in range(self.length))
        return password

    def adding_characters(self, characters: str, to_use: bool, to_add: str) -> str:
        """Concatenates a new string to an existing set of characters if the user selects to use them
        Args:
            characters (str): The base set of characters to use
            to_use (bool): User selection for whether to join the two strings together
            to_add (str): the characters to add to the original set of characters
        Returns:
            str: The set of valid characters to use when creating a password
        """
        return characters + to_add if to_use else characters
