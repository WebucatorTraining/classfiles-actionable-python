import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        roll = random.randint(1, self.sides)
        return roll