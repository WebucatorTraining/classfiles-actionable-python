import datetime

# Creating times
midnight = datetime.time()
print(midnight)
noon = datetime.time(12)
print(noon)
t1 = datetime.time(1, 2, 3, 4)
print(t1)
t2 = datetime.time(hour=14,
                   minute=13,
                   second=12,
                   microsecond=11)
print(t2)

h = t2.hour
m = t2.minute
s = t2.second
ms = t2.microsecond

print('The time is {}:{}:{}.{}.'.format(h, m, s, ms))

# Time methods
t2_new = t2.replace(hour=4)
print(t2_new)

str_t2 = t2.strftime('%I:%M %p')
print(str_t2)