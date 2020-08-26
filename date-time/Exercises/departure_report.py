from datetime import datetime

def get_departures():
    departures = []
    with open('../data/departure-data.txt') as f:
        for line in f.read().splitlines():
            departure = get_departure(line)
            if departure:
                departures.append(departure)
    return departures

def get_departure(line):
    """Return a tuple containing two  datetime objects."""

    # If the line begins with an asterisk (*), return None

    # Get the planned and actual departures as strings by
    # splitting the line on a tab character into a list
    # Assign the first item in the list to planned and the
    # second item to actual

    # Convert the planned departure time to a datetime and
    # assign the result to date_planned

    # For those lines that have an actual departure time,
    # convert the actual departure time to a datetime and
    # assign the result to date_actual.
    # For lines that don't have an actual departure date, assign
    # None to date_actual.

    # Return a tuple with date_planned and date_actual.
    return (date_planned, date_actual)

def left_ontime(departure):
    planned = departure[0]
    actual = departure[1]
    if not actual:
        return False
    return actual == planned

# Write the following four functions. They should
# all return a boolean value
def left_early(departure):
    pass

def left_late(departure):
    pass

def left_next_day(departure):
    pass

def did_not_run(departure):
    pass

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