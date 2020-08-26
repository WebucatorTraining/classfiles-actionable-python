import random

def get_word():
    """Returns random word."""
    words = ['Charlie', 'Woodstock', 'Snoopy', 'Lucy', 'Linus',
             'Schroeder', 'Patty', 'Sally', 'Marcie']
    return random.choice(words).upper()

def check(word, guesses):
    """Creates and returns string representation of word
    displaying asterisks for letters not yet guessed."""
    status = '' # Current status of guess
    last_guess = guesses[-1]
    matches = 0 # Number of occurrences of last_guess in word

    for letter in word:
        status += letter if letter in guesses else '*'

        if letter == last_guess:
            matches += 1

    if matches > 1:
        print('The word has {} "{}"s.'.format(matches, last_guess))
    elif matches == 1:
        print('The word has one "{}".'.format(last_guess))
    else:
        print('Sorry. The word has no "{}"s.'.format(last_guess))

    return status

def main():
    word = get_word() # The random word
    n = len(word) # The number of letters in the random word
    guesses = [] # The list of guesses made so far
    guessed = False
    print('The word contains {} letters.'.format(n))

    while not guessed:
        guess = input('Guess a letter or a {}-letter word: '.format(n))
        guess = guess.upper()
        if guess in guesses:
            print('You already guessed "{}".'.format(guess))
        elif len(guess) == n: # Guessing whole word
            guesses.append(guess)
            if guess == word:
                guessed = True
            else:
                print('Sorry, that is incorrect.')
        elif len(guess) == 1: # Guessing letter
            guesses.append(guess)
            result = check(word, guesses)
            if result == word:
                guessed = True
            else:
                print(result)
        else: # guess had wrong number of characters
            print('Invalid entry.')

    print('{} is it! It took {} tries.'.format(word, len(guesses)))

main()