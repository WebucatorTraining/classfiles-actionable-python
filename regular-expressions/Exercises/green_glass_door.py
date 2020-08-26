def green_glass_door(word):
    prev_letter = ''
    for letter in word:
        letter = letter.upper()
        if letter == prev_letter:
            return True
        prev_letter = letter
    return False

fruits = ['banana', 'apple', 'pear', 'grape', 'cherry',
          'persimmons', 'orange', 'passion fruit']

for fruit in fruits:
    if green_glass_door(fruit):
        print(f'YES! {fruit} can pass through the green glass door.')
    else:
        print(f'NO! {fruit} cannot pass through the green glass door.')