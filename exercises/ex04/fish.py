"""File to define Fish class."""

__author__ = "730579218"


class Fish:
    """A class representing a fish in the river ecosystem."""
    age: int

    def __init__(self):
        """Initialize a fish with age 0."""
        self.age = 0
    
    def one_day(self):
        """Simulate one day of aging for the fish."""
        self.age += 1
