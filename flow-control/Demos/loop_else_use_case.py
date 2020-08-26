BLACK_LIST = [
    'shitake',
    'sugar',
    'fudge',
    'gosh',
    'darn',
    'dang',
    'heck'
]

def main():
    sentence = input('Input a sentence: ')
    
    for word in sentence.split():
        if word in BLACK_LIST:
            print('You used a naughty word.')
            break
    else:
        print('Sentence passes cleanliness test.')

main()