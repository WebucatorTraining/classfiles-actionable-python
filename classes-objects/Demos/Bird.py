from FlyingObject import FlyingObject

class Bird(FlyingObject):
    _birds = []
    def __init__(self, name):
        super().__init__(name)
        type(self)._birds.append(self)
        self._healthy_wings = True

    def take_off(self):
        if self.healthy_wings:
            super().take_off()

    def land(self):
        super().land()
    
    @classmethod
    def birds(cls):
        return cls._birds
    
    @property
    def healthy_wings(self):
        return self._healthy_wings 

    @healthy_wings.setter
    def healthy_wings(self, healthy):
        self._healthy_wings = healthy