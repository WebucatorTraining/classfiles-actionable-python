# while loop
num = 0
while num < 6:
    print(num)
    num += 1

# for loops with ranges
for num in range(6):
    print(num)

for num in range(0, 6):
    print(num)

for num in range(1, 11, 2):
    print(num)

for num in range(10, 0, -1):
    print(num)

# Looping through a list
nums = [0, 1, 2, 3, 4, 5] # list
for num in nums:
    print(num)

# Looping through a tuple
nums = (0, 1, 2, 3, 4, 5) # tuple
for num in nums:
    print(num)

# Looping through a dictionary
grades = {'English':97, 'Math':93, 'Art':74, 'Music':86}

for course in grades:
    print(course)

for course in grades.keys():
    print(course)

for grade in grades.values():
    print(grade)

for course, grade in grades.items():
    print(f'{course}: {grade}')

for item in grades.items():
    course = item[0]
    grade = item[1]
    print(f'{course}: {grade}')

# break
for num in range(11, 20):
    print(num)
    if num % 5 == 0:
        break

# continue
for num in range(1, 12):
    if num % 5 == 0:
        continue
    print(num)