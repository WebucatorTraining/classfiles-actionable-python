import random
import time

start_time = time.perf_counter()
numbers = str(random.randint(1, 100))
for i in range(1000):
    num = random.randint(1, 100)
    numbers += ',' + str(num)
end_time = time.perf_counter()
td1 = end_time - start_time

start_time = time.perf_counter()
numbers = [str(random.randint(1, 100)) for i in range(1000)]
numbers = ', '.join(numbers)
end_time = time.perf_counter()
td2 = end_time - start_time

print(f"""Time Delta 1: {td1}
Time Delta 2: {td2}""")