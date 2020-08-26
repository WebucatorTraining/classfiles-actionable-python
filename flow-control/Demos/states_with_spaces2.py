def main():
    with open('../data/states.txt') as f:
        lines = f.read().splitlines()

    states = [line.split('\t')[0] for line in lines]
    states_with_spaces = [state for state in states if ' ' in state]

    # Print the states_with_spaces list
    for i, state_name in enumerate(states_with_spaces, 1):
        print(f'{i}. {state_name}')

main()