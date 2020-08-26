def is_valid_age(s):
    return s.isdigit() and 1 <= int(s) <= 113

def main():
    age = input('How old are you? ')
    while not is_valid_age(age):
        age = input('Please enter a real age as a number: ')

    age = int(age)
    if age >= 21:
        print('You can vote and drink.')
    elif age >= 18:
        print('You can vote, but can\'t drink.')
    else:
        print('You cannot vote or drink.')

main()