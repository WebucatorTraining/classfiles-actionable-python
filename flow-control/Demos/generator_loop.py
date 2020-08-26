import random

def get_rand_nums(low, high, num):
    for number in range(num):
        yield random.randint(low, high)

numbers = get_rand_nums(1, 100, 5)

print('First time through:')
for num in numbers:
    print(num)

print('Second time through:')
for num in numbers:
    print(num)