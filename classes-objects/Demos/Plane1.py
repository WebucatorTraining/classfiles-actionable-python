class Plane:
    planes = []
    def __init__(self):
        self._in_air = False
        type(self).planes.append(self)
    
    def take_off(self):
        self._in_air = True
    
    def land(self):
        self._in_air = False
    
    @classmethod
    def num_planes(cls):
        return len(cls.planes)
    
    @classmethod
    def num_planes_in_air(cls):
        return len([plane for plane in cls.planes if plane._in_air])