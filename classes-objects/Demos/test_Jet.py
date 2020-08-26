# Test Jet class:

from Plane import Plane
from Jet import Jet

p1 = Plane()
p2 = Plane()
p3 = Plane()
p1.take_off()
p2.take_off()
p1.land()
p4 = Jet()
p4.take_off()
print(Plane.num_planes(), Plane.num_planes_in_air())