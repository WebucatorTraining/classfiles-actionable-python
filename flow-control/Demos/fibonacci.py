def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def main():
    for i in fibonacci():
        print(i)
        if input('Enter for next or q to quit: ') == 'q':
            print('Goodbye!')
            break

main()