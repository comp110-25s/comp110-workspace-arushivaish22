"""File to define Bear class.""" 

__author__ = "730579218"


class Bear:
    """A class representing a bear in a river ecosystem."""
    age: int
    hunger_score: int

    def __init__(self):
        """Initialize a bear with age 0 and hunger 0."""
        self.age = 0 
        self.hunger_score = 0
    
    def one_day(self):
        """Simulates one dat of aging and one hunger score increase."""
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int): 
        """Increase the bear's hunger score by number of fish eaten."""
        self.hunger_score += num_fish
