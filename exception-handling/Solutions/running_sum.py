def main():
    total = 0
    while True:
        try:
            num = input('Enter a number: ')
            if num.lower() == 'q':
                print('Goodbye!')
                break
            num = int(num) # This might cause an error
        except ValueError:
            print('Integers only please. Try again.')
        else:
            total += num
            print('The current total is:', total)

main()