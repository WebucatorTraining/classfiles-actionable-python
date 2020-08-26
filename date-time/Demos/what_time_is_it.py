import time

seconds_since_epoch = time.time()
minutes_since_epoch = seconds_since_epoch / 60
hours_since_epoch = minutes_since_epoch / 60
days_since_epoch = hours_since_epoch / 24
years_since_epoch = days_since_epoch / 365.25

print("""s: {:,}
m: {:,}
h: {:,}
d: {:,}
y: {:,}""".format(seconds_since_epoch,
                  minutes_since_epoch,
                  hours_since_epoch,
                  days_since_epoch,
                  years_since_epoch, sep='\n'))