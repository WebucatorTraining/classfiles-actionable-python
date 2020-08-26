import csv

def get_data_as_list_from_csv(csvfile):
    with open(csvfile, newline='', encoding="utf-8") as csvfile:
        data = csv.DictReader(csvfile)
        return list(data)

def get_population(data, state, year):
    # Loop through data
    for row in data:
        # Is this the row that matches the passed-in state?
        if row['State'] == state:
            # Return the value for the column for the passed in year
            return row[year]
    return None # No matching state found

def main():
    data = get_data_as_list_from_csv('../data/population-by-state.csv')
    state = input('State name: ')
    year = input('Year between 2010 and 2020: ')
    population = get_population(data, state, year)
    if population:
        print(f'{state}\'s population in {year}: {population}.')
    else:
        print(f'No state found matching "{state}".')

main()