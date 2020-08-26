def main():
    total = 0
    while True:
        num = input('Enter a number (q to quit): ')

        if num.lower() == 'q':
            print('Goodbye!')
            break

        if not num.isdigit():
            print('Integers only please. Try again.')
        else:
            total += int(num)
            print('The current total is:', total)

main()