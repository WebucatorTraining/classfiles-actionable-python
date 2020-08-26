from collections import Counter
from Die3 import Die

die = Die()

for i in range(100000):
    roll = die.roll()

rolls = die.rolls
c = Counter(rolls)
c_sorted = sorted(c.items())

print(c_sorted)