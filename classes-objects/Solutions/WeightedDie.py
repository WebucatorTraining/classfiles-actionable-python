import random

from Die import Die

class WeightedDie(Die):
    "A weighted die"
    def __init__(self, weights, sides=6):
        """Creates a new weighted die
        
        Keyword arguments:
        sides (int) -- number of die sides.
        weights (list) -- a list of integers holding the weights 
            for each die side
        """
        if len(weights) != sides:
            raise Exception(f'weights must be a list of length {sides}.')
        super().__init__(sides)
        self._weights = weights
    
    def roll(self):
        """Returns a value between 1 and the number of die sides."""
        options = []
        for i in range(self._sides):
            for j in range(self._weights[i]):
                options.append(i+1)
        roll = random.choice(options)
        self._rolls.append(roll)
        return roll