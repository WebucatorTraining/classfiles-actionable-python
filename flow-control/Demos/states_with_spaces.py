def main():
    with open('../data/states.txt') as f:
        lines = f.read().splitlines()

    states_with_spaces = []

    for line in lines:
        # Split the line into a 2-item list containing the
        #   state name and abbreviation
        state = line.split('\t')

        # If the state name has a space, add it to states_with_spaces
        if ' ' in state[0]:
            states_with_spaces.append(state[0])

    # Print the states_with_spaces list
    for i, state_name in enumerate(states_with_spaces, 1):
        print(f'{i}. {state_name}')

main()