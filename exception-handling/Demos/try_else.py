def square_num():
    try:
        num = int(input('Input Integer: '))
    except ValueError:
        print('That is not an integer.')
    else:
        print(num, 'squared is', num**2)

def cube_num():
    num = input('Input Number: ')
    if num.isdigit():
        print(num, 'cubed is', int(num)**3)
    else:
        print('That is not an integer.')