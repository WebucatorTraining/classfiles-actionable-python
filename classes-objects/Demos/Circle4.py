import math

class Circle:
    def __init__(self, val, prop='r'):
        if prop == 'r':
            self.set_radius(val)
        elif prop == 'd':
            self.set_diameter(val)
        elif prop == 'c':
            self.set_circumference(val)
        elif prop == 'a':
            self.set_area(val)
        else:
            raise Exception('prop must be r, d, c, or a')

    def resize_by(self, amount):
        r = self._radius * (1 + amount)
        self.set_radius(r)

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, r):
        self._radius = r
        self._diameter = r * 2
        self._circumference = r * 2 * math.pi
        self._area = r ** 2 * math.pi

    @property
    def diameter(self):
        return self._diameter

    @diameter.setter
    def diameter(self, d):
        self.radius = d / 2

    @property
    def circumference(self):
        return self._circumference

    @circumference.setter
    def circumference(self, c):
        self.radius = c / (2 * math.pi)

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, a):
        self.radius = (a / math.pi) ** .5