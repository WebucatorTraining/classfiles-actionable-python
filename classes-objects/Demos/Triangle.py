class Triangle:
    def __init__(self, sides):
        if not self.is_triangle(sides):
            raise Exception('Cannot make triangle with those sides.')
        self._sides = sides
    
    @property
    def perimeter(self):
        return sum(self._sides)
    
    @property
    def area(self):
        p = self.perimeter/2
        a = self._sides[0]
        b = self._sides[1]
        c = self._sides[2]
        return ( p * (p-a) * (p-b) * (p-c) ) ** .5
        
    @staticmethod
    def is_triangle(sides):
        if len(sides) != 3:
            return False
        sides.sort()
        if sides[0] + sides[1] < sides[2]:
            return False
        return True