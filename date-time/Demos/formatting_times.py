import time

epoch = time.gmtime(0)
print(time.strftime('%c', epoch)) # 01/01/70 00:00:00
print(time.strftime('%x', epoch)) # 01/01/70
print(time.strftime('%X', epoch)) # 00:00:00
print(time.strftime('%A, %B %d, %Y, %I:%M %p', epoch))
# Thursday, January 01, 1970, 12:00 AM

independence_day = time.strptime('07/04/1776', '%m/%d/%Y')
print(independence_day)