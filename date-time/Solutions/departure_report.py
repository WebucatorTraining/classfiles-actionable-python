from datetime import datetime

def get_departures():
    """Return a list of departures."""
    departures = []
    with open('../data/departure-data.txt') as f:
        for line in f.read().splitlines():
            departure = get_departure(line)
            if departure:
                departures.append(departure)
    return departures

def get_departure(line):
    """Return a tuple containing two datetime objects."""

    if line[0] == '*':
        return None

    departure = line.split('\t')
    planned = departure[0]
    actual = departure[1]

    date_planned = datetime.strptime(planned, '%m/%d/%Y %I:%M %p')

    if actual:
        date_actual = datetime.strptime(actual, '%m/%d/%Y %I:%M %p')
    else: # Date doesn't exist
        date_actual = None

    return (date_planned, date_actual)

def left_ontime(departure):
    """Return True if left ontime. False, otherwise."""
    planned = departure[0]
    actual = departure[1]
    if not actual:
        return False
    return actual == planned

def left_early(departure):
    """Return True if left early. False, otherwise."""
    planned = departure[0]
    actual = departure[1]
    if not actual:
        return False
    if actual < planned:
        print('Early:', departure)
    return actual < planned

def left_late(departure):
    """Return True if left late. False, otherwise."""
    planned = departure[0]
    actual = departure[1]
    if not actual:
        return False
    return actual > planned

def left_next_day(departure):
    """Return True if departed next day. False, otherwise."""
    planned = departure[0]
    actual = departure[1]
    if not actual:
        return False
    return actual.day > planned.day

def did_not_run(departure):
    """Return True if did not depart. False, otherwise."""
    return not departure[1]

def main():
    departures = get_departures()
    ontime_departures = [d for d in departures if left_ontime(d)]
    early_departures = [d for d in departures if left_early(d)]
    late_departures = [d for d in departures if left_late(d)]
    next_day_departures = [d for d in departures if left_next_day(d)]
    cancelled_trips = [d for d in departures if did_not_run(d)]

    print(f"""Total Departures: {len(departures)}
Ontime Departures: {len(ontime_departures)}
Early Departures: {len(early_departures)}
Late Departures: {len(late_departures)}
Next Day Departures: {len(next_day_departures)}
Cancelled Trips: {len(cancelled_trips)}""")

main()