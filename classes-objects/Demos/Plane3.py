from FlyingObject import FlyingObject

class Plane(FlyingObject):
    _planes = []
    _flying_objects = []
    def __init__(self, name):
        super().__init__(name)
        type(self)._planes.append(self)
        self._over_land = True
    
    def take_off(self):
        super().take_off()

    def land(self):
        if self.over_land:
            super().land()
    
    @classmethod
    def planes(cls):
        return cls._planes
    
    @property
    def over_land(self):
        return self._over_land 

    @over_land.setter
    def over_land(self, over_land):
        self._over_land = over_land