def main():
    with open('../data/states.txt') as f:
        states = f.read().splitlines()
    
    print(f'The file contains {len(states)} states.')

main()