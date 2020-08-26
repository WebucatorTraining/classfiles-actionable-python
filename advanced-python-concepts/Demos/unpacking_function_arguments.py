import math
def distance_from_origin(a,b):
    return math.sqrt(a**2 + b**2)

# Calling the function:
c = distance_from_origin(3, 4)
print('Calling the function with literals:', c,'-'*70,sep='\n')

# Trying to pass a tuple to the function, this will cause an error:
"""point = (3, 4)
c = distance_from_origin(point)
print(c)
"""

# Unpacking the tuple ourselves:
point = (3,4)
c = distance_from_origin(point[0], point[1])
print('Unpacking the tuple ourselves:', c,'-'*70,sep='\n')

# Using an asterisk to unpack tuple:
point = (3, 4)
c = distance_from_origin(*point)
print('Using an asterisk to unpack the tuple:', c,'-'*70,sep='\n')