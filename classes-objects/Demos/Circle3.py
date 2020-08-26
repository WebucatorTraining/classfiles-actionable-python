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

    def set_radius(self, r):
        self._radius = r
        self._diameter = r * 2
        self._circumference = r * 2 * math.pi
        self._area = r ** 2 * math.pi

    def get_radius(self):
        return self._radius

    def set_diameter(self, d):
        self.set_radius(d / 2)

    def get_diameter(self):
        return self._diameter

    def set_circumference(self, c):
        self.set_radius(c / (2 * math.pi))

    def get_circumference(self):
        return self._circumference

    def set_area(self, a):
        self.set_radius((a / math.pi) ** .5)

    def get_area(self):
        return self._area

    def resize_by(self, amount):
        r = self._radius * (1 + amount)
        self.set_radius(r)