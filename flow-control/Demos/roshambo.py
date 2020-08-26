import random

def roshambo(weapons):
    while True:
        yield random.choice(weapons)

def play(weapons, choice, python_weapons):
    your_weapon = weapons[int(choice)-1]
    python_weapon = next(python_weapons)

    if your_weapon == python_weapon:
        print('Tie: You both chose', your_weapon)
    elif ((your_weapon == 'Scissors' and python_weapon == 'Paper')
          or (your_weapon == 'Paper' and python_weapon == 'Rock')
          or (your_weapon == 'Rock' and python_weapon == 'Scissors')):
        print('You win:', your_weapon, 'beats', python_weapon)
    else:
        print('You lose:', python_weapon, 'beats', your_weapon)
    print('--------')


def make_choice():
    choice = input("""Choose your weapon:
1: Rock
2: Paper
3: Scissors
q: Quit
""")
    return choice

def main():
    weapons = ['Rock', 'Paper', 'Scissors']
    python_weapons = roshambo(weapons)
    choice = make_choice()
    while choice in ['1', '2', '3']:
        play(weapons, choice, python_weapons)
        choice = make_choice()
    print('Goodbye!')

main()