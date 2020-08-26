from collections import Counter
from Die1 import Die

die = Die()

rolls = []
for i in range(100000):
    roll = die.roll()
    rolls.append(roll)
    
c = Counter(rolls)
c_sorted = sorted(c.items())

print(c_sorted)