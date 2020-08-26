def main():
    with open('../data/states.txt') as f:
        lines = f.read().splitlines()

    states_with_spaces = [
        line.split('\t')[0] # Get state
        for line in lines # For each line
        if ' ' in line.split('\t')[0] # Where there is a space in state
    ]

    # Print the states_with_spaces list
    for i, state_name in enumerate(states_with_spaces, 1):
        print(f'{i}. {state_name}')

main()