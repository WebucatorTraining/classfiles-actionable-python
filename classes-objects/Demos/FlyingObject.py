import abc

class FlyingObject(metaclass=abc.ABCMeta):
    _flyingobjects = []
    def __init__(self, name):
        self._in_air = False
        self.name = name
        type(self)._flyingobjects.append(self)
    
    @abc.abstractmethod
    def take_off(self):
        self._in_air = True
    
    @abc.abstractmethod
    def land(self):
        self._in_air = False
    
    @classmethod
    def flying_objects(cls):
        return cls._flyingobjects

    def __str__(self):
        return self.name