import re
import random

def get_word():
    words = ['Charlie', 'Woodstock', 'Snoopy', 'Lucy', 'Linus',
             'Schroeder', 'Patty', 'Sally', 'Marcie']
    return random.choice(words).upper()

def green_glass_door_1():
    word = get_word()
    prev_letter = ''
    for letter in word:
        letter = letter.upper()
        if letter == prev_letter:
            return True
        prev_letter = letter
    return False

def green_glass_door_2():
    word = get_word()
    pattern = re.compile(r'(.)\1')
    return pattern.search(word)