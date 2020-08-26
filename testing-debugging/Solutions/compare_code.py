import re
import random
from timeit import repeat

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

tds1 = repeat(green_glass_door_1, number=1000, repeat=4, globals=globals())
tds2 = repeat(green_glass_door_2, number=1000, repeat=4, globals=globals())

print(tds1, tds2, sep="\n")
print('-' * 70)

print('green_glass_door_1 compared to green_glass_door_2:')
print('{:.2%}'.format(sum(tds1)/sum(tds2)))