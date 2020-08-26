import random

def bingo():
    balls = {
        'B': list(range(1, 16)),
        'I': list(range(16, 31)),
        'N': list(range(31, 46)),
        'G': list(range(46, 61)),
        'O': list(range(61, 76))
    }
        
    while balls:
        letter = random.choice(list(balls.keys()))
        number = random.choice(balls[letter])
        balls[letter].remove(number) # Remove number from letter list
        if not balls[letter]: # Letter has no more numbers
            print('Removing', letter)
            del balls[letter] # Delete letter from dictionary
        yield (letter, number)

def main():
    for ball in bingo():
        print(ball)
        if input('Enter for next ball or q to quit') == 'q':
            print('Goodbye!')
            break
    else:
        print('All out of balls.')

main()