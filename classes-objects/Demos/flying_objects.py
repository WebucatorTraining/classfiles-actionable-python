from Plane import Plane3
from Bird import Bird
from FlyingObject import FlyingObject

p1 = Plane('Spirit of St. Louis')
p2 = Plane('Air Force One')
b1 = Bird('Big Bird')
b2 = Bird('Roadrunner')
b2.healthy_wings = False
b3 = Bird('Tweety')

p1.take_off()
p1.over_land = False
p1.land()

b1.take_off()
b2.take_off()

print('Flying Objects:')
for object in p1.flying_objects():
    print(object)
print('-----------')

print('Planes:')
for plane in p1.planes():
    print(plane)
print('-----------')

print('Birds:')
for bird in b1.birds():
    print(bird)