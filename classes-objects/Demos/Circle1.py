import math

class Circle:
    def __init__(self, val, prop='r'):
        if prop == 'r': # radius
            self.radius = val
        elif prop == 'd': # diameter
            self.radius = val / 2
        elif prop == 'c': # circumference
            self.radius = val / (2 * math.pi)
        elif prop == 'a': # area
            self.radius = (val / math.pi) ** .5
        else:
            raise Exception('prop must be r, d, c, or a')
        
        self.diameter = self.radius * 2
        self.circumference = self.radius * 2 * math.pi
        self.area = self.radius ** 2 * math.pi