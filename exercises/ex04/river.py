"""File to define River class."""

__author__ = "730579218"

from exercises.EX04.fish import Fish
from exercises.EX04.bear import Bear


class River:
    """A class representing a river."""
    day: int
    bears: list
    fish: list
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears.""" 
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Remove fish older than 3 and bears older than 5."""
        surviving_fish: list[Fish] = []
        for fish in self.fish:
            if fish.age <= 3:
                surviving_fish.append(fish)
        self.fish = surviving_fish

        surviving_bears: list[Bear] = []
        for bear in self.bears:
            if bear.age <= 5:
                surviving_bears.append(bear)
        self.bears = surviving_bears

    def bears_eating(self):
        """Feed bears if 5 or more fish are available; else, decrease hunger."""
        for bear in self.bears: 
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
    
    def check_hunger(self):
        """Remove Bears with hunger_score below 0."""
        surviving_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                surviving_bears.append(bear)
        self.bears = surviving_bears
        
    def repopulate_fish(self):
        """Repopulate fish: every 2 fish produce 4 new fish."""
        num_new_fish = (len(self.fish) // 2) * 4
        for _ in range(num_new_fish):
            self.fish.append(Fish())
    
    def repopulate_bears(self):
        """Repopulate Bears: every 2 bears produce 1 new bear."""
        num_new_bears = len(self.bears) // 2
        for _ in range(num_new_bears): 
            self.bears.append(Bear())
    
    def view_river(self):
        """Print the current river day and population counts."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish Population: {len(self.fish)}")
        print(f"Bear Population: {len(self.bears)}")
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
    
    def one_river_week(self): 
        """Simulate one week of life at the river."""
        for _ in range(7): 
            self.one_river_day()

    def remove_fish(self, amount: int):
        """Remove the first amount fish from the river."""
        for _ in range(amount): 
            if len(self.fish) > 0: 
                self.fish.pop(0)

            
