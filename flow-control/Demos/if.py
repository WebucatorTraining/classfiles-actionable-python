def main():
    age = int(input('How old are you? '))

    if age >= 21:
        print('You can vote and drink.')
    elif age >= 18:
        print('You can vote, but can\'t drink.')
    else:
        print('You cannot vote or drink.')

main()