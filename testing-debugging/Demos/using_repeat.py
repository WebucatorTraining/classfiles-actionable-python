import random
from timeit import repeat

str_nums1 = """
numbers = str(random.randint(1, 100))
for i in range(1000):
    num = random.randint(1, 100)
    numbers += ', ' + str(num)"""
    
str_nums2 = """
numbers = [str(random.randint(1, 100)) for i in range(1000)]
numbers = ', '.join(numbers)"""

tds1 = repeat(str_nums1, number=1000, repeat=4, globals=globals())
tds2 = repeat(str_nums2, number=1000, repeat=4, globals=globals())

print("Results from using repeat()")
print(tds1, tds2, sep="\n")
print('-' * 70)

print('str_nums1 compared to str_nums2:')
print(f'{sum(tds1)/sum(tds2):.2%}')