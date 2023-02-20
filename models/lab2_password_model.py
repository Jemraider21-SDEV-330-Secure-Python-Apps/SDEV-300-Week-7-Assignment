from dataclasses import dataclass

@dataclass
class Lab2PasswordModel:
    """Model for generating secure password
    """
    length:int
    lowercase:bool
    uppercase:bool
    numbers:bool
    specials:bool