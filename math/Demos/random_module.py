import random

# random.random()
print(random.random())
print(random.random())
print(random.random())

# random.randint()
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))

# random.randrange()
print(random.randrange(10))
print(random.randrange(1, 10))
print(random.randrange(1, 10, 2))

# random.uniform()
print(random.uniform(1, 10))
print(random.uniform(1, 10))
print(random.uniform(1, 10))

# Seeding
seed = 1234
random.seed(seed)

for a in range(1, 5):
    print(random.randint(1, 10))