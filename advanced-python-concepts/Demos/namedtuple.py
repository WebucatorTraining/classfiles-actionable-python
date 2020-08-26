from collections import namedtuple

Point = namedtuple('Point', 'x, y')

# Set target position:
target_pos = Point(100, 200)

# Get x value of target position
print(target_pos.x)