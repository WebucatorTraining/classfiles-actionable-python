def main():
    print('Example 1: for loop')
    num = int(input('Enter a number: '))
    for i in range(5):
        if i == num:
            break
        print(i)
    else:
        print(f'Completed iterating without reaching {num}.')

    print('\nExample 2: while loop')
    i = 0
    num = int(input('Enter a number: '))
    while i <= 5:
        if i == num:
            break
        print(i)
        i += 1
    else:
        print(f'Completed iterating without reaching {num}.')

main()