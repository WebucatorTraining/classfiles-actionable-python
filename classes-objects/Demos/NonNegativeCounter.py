from collections import Counter

class NonNegativeCounter(Counter):
    'Counter that disallows negative values'
    def __setitem__(self, key, value):
        value = 0 if value < 0 else value
        super().__setitem__(key, value)