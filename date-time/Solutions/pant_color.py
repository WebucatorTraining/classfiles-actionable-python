from datetime import datetime

def is_summer(the_date=datetime.now()):
    # Get the year of the passed-in datetime.datetime object
    year = the_date.year

    # Create datetime.datetime objects for starts of seasons
    summer_start = datetime(year, 6, 20)
    fall_start = datetime(year, 9, 22)

    # Return true if passed-in date is between starts of seasons
    return (summer_start < the_date < fall_start)

def main():
    # Use ternary operator to assign pant color
    pant_color = 'white' if is_summer() else 'black'
    print(f'You should wear {pant_color} pants.')

main()