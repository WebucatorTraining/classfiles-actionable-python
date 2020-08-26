def is_state(state):
    with open('../data/states.txt') as f:
        states = f.read().splitlines()

    state_abbreviations = []
    for state_row in states:
        state_abbreviation = state_row.split('\t')[1]
        state_abbreviations.append(state_abbreviation)

    return state in state_abbreviations

def main():
    print('Name as many state abbreviations do you know?')
    print('Separate them with spaces:')
    states = input('').split()
    for state in states:
        state = state.upper()
        if not is_state(state):
            print(f'{state} is not a state.')
            break
    else:
        print(f'You named {len(states)} states.')

main()