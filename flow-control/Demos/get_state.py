def get_state(abbreviation):
    # Read the data from the file into a list
    with open('../data/states.txt') as f:
        states = f.read().splitlines()
    
    # Loop through the list
    for state_row in states:
        # Split each row on the tab character into a
        #   two-element list
        state = state_row.split('\t')

        # If the 2nd element matches the passed-in abbreviation
        #   return the first element
        if state[1] == abbreviation.upper():
            return state[0]
    
    # If no state matched the abbreviation, return None
    return None

def main():
    # Loop until break statement
    while True:
        abbr = input('State abbreviation (q to quit): ').upper()

        # Allow user to break loop by entering "Q"
        if abbr == 'Q':
            print('Goodbye!')
            break

        # Get state name from abbreviation
        state = get_state(abbr)

        # Inform the user what state, if any, maps to the abbreviation
        if state:
            print(f'"{abbr}" is the abbreviation for {state}.')
        else:
            print(f'No state has "{abbr}" as an abbreviation.')

main()