from dataclasses import dataclass


@dataclass
class Lab1Model:
    """Model the data for voting user registration
    """
    name: str
    age: int
    state: str
    zipcode: int
