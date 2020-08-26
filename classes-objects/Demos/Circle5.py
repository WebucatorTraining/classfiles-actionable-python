class Circle:
    "A circle"
    def __init__(self, val, prop='r'):
        """Create a circle based on a radius, diameter, 
            circumference, or area

        Keyword arguments:
        val (float) -- the value of prop
        prop (str)
            -- 'r' : radius (default)
            -- 'd' : diameter
            -- 'c' : circumference
            -- 'a' : area
        """
        self._radius = None
        self._diameter = None
        self._circumference = None
        self._area = None
        if prop == 'r':
            self.radius = val
        elif prop == 'd':
            self.diameter = val
        elif prop == 'c':
            self.circumference = val
        elif prop == 'a':
            self.area = val
        else:
            raise Exception('prop must be r, d, c, or a')

    @property
    def radius(self):
        "radius of the circle object"
        return self._radius
    
    @radius.setter
    def radius(self, r):
        """sets _radius, _diameter, _circumference, and _area of 
			circle object"""
        self._radius = r
        self._diameter = r * 2
        self._circumference = r * 2 * math.pi
        self._area = r ** 2 * math.pi
    
    @property
    def diameter(self):
        "diameter (2 x r) of the circle object"
        return self._diameter
    
    @diameter.setter
    def diameter(self, d):
        """uses diameter d to set radius, which then 
         updates all related pseudo-private attributes"""
        self.radius = d / 2
    
    @property
    def circumference(self):
        "circumference (PI x d) of the circle object"
        return self._circumference
    
    @circumference.setter
    def circumference(self, c):
        """uses circumference c to set radius, which then updates
         all related pseudo-private attributes"""
        self.radius = c / (2 * math.pi)
    
    @property
    def area(self):
        "area (PI x r squared) of the circle object"
        return self._area
    
    @area.setter
    def area(self, a):
        """uses area a to set radius, which then updates all
         related pseudo-private attributes"""
        self.radius = (a / math.pi) ** .5
    
    def resize_by(self, amount):
        """resizes radius, which then updates all related 
			pseudo-private attributes

        Keyword arguments:
        amount (float) -- the amount by which to resize the radius
                       -- a negative number shrinks the radius
        """
        self.radius = self.radius * (1 + amount)