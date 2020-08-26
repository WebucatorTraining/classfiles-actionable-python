import datetime

# 2010 Iditarod
racetime = datetime.timedelta(days=8,
                              hours=23,
                              minutes=49,
                              seconds=9)

print(racetime.total_seconds())

finish = datetime.datetime(year=2010,
                           month=3,
                           day=16,
                           hour=14,
                           minute=59)

start = finish - racetime
print(start)