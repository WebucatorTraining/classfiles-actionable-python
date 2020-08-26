def odd_numbers():
    i = -1
    while True:
      i += 2
      yield i

def main():
    for i in odd_numbers():
        print(i)
        if input('Enter for next or q to quit: ') == 'q':
            print('Goodbye!')
            break

main()