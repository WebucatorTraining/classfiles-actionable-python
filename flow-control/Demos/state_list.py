def main():
    with open('../data/states.txt') as f:
        states = f.read().splitlines()

    for i, state in enumerate(states, 1):
        state_name = state.split('\t')[0]
        print(f'{i}. {state_name}')

main()