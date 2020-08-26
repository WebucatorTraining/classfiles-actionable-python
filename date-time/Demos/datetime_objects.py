import datetime

# Creating datetimes
moonwalk = datetime.datetime(year=1969,
                             month=7,
                             day=21,
                             hour=2,
                             minute=56,
                             second=15,
                             tzinfo=datetime.timezone.utc)

print(moonwalk)

m = moonwalk.month
d = moonwalk.day
y = moonwalk.year
h = moonwalk.hour
n = moonwalk.minute
s = moonwalk.second
ms = moonwalk.microsecond

print('Armstrong stepped onto the ' +
      'moon at {}:{}:{}.{} on {}/{}/{}.'.format(h, n, s, ms, m, d, y))

today = datetime.datetime.today()
print(today)

now = datetime.datetime.now()
print(now)

# Datetime methods

mw_50_anniversary = moonwalk.replace(year=2019)
print(mw_50_anniversary)
print(mw_50_anniversary.timestamp())

print(moonwalk.weekday())
print(moonwalk.ctime())

str_moonwalk = moonwalk.strftime('%A, %B %d, %Y, %I:%M %p')
print(str_moonwalk)