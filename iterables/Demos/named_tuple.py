from collections import namedtuple

Point = namedtuple('point', 'x, y')

mouse_pos = Point(100, 200)
print("X Position of Mouse:", mouse_pos.x)