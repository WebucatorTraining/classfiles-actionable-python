import datetime
import time

independence_day = datetime.date(1776, 7, 4)
today = datetime.date.today()
today2 = datetime.date.fromtimestamp(time.time())
epoch_offset = datetime.date.fromtimestamp(0)

print(independence_day)
print(today)
print(today2)
print(epoch_offset)

# date attributes
m = independence_day.month
d = independence_day.day
y = independence_day.year

print('Today is {}/{}/{}.'.format(m, d, y))

# date methods
tj_dies = independence_day.replace(year=1826)
print(tj_dies)

t = independence_day.timetuple()
print(t)

wd = independence_day.weekday()
print(wd)

str_i_day1 = independence_day.ctime()
print(str_i_day1)

str_i_day2 = independence_day.strftime('%A, %B %d, %Y, %I:%M %p')
print(str_i_day2)