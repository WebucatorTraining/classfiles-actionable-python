def main():
    age = int(input('How old are you? '))

    is_citizen = (input('Are you a citizen? Y or N ').lower() == 'y')

    if age >= 21 and is_citizen:
        print('You can vote and drink.')
    elif age >= 21:
        print('You can drink, but can\'t vote.')
    elif age >= 18 and is_citizen:
        print('You can vote, but can\'t drink.')
    else:
        print('You cannot vote or drink.')

main()