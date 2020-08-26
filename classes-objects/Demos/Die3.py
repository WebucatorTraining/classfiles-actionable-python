import random

class Die:
    def __init__(self, sides=6):
        if type(sides) != int or sides < 1:
            raise Exception('sides must be a positive integer.')
        self._sides = sides
        self._rolls = []
    
    @property
    def rolls(self):
        return self._rolls
        
    def roll(self):
        roll = random.randint(1, self._sides)
        self._rolls.append(roll)
        return roll