import time
import random

iterations = int(input('Number of iterations: '))

# Concatenating strings
start_time = time.perf_counter()
numbers = ''
for i in range(iterations):
    num = random.randint(1, 100)
    numbers += ',' + str(num)
end_time = time.perf_counter()
td1 = end_time - start_time

# Appending to a list
start_time = time.perf_counter()
numbers = []
for i in range(iterations):
    num = random.randint(1, 100)
    numbers.append(str(num))
numbers = ', '.join(numbers)
end_time = time.perf_counter()
td2 = end_time - start_time

# Using a list comprehension
start_time = time.perf_counter()
numbers = [str(random.randint(1, 100)) for i in range(1, iterations)]
numbers = ', '.join(numbers)
end_time = time.perf_counter()
td3 = end_time - start_time

print(f"""Number of numbers: {iterations:,}
Time Delta 1: {td1}
Time Delta 2: {td2}
Time Delta 3: {td3}
td1 is {round(td1/td3, 2)}x slower than td3.\n""")