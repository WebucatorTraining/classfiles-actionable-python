fruit = ['apple', 'orange', 'banana', 'pear', 'lemon', 'watermelon']

first_5_fruit = fruit[0:5]
# ['apple', 'orange', 'banana', 'pear', 'lemon']
print(first_5_fruit)

fruit_2_thru_4 = fruit[1:4]
# ['orange', 'banana', 'pear']
print(fruit_2_thru_4)

fruit_5_to_end = fruit[4:]
# ['lemon', 'watermelon']
print(fruit_5_to_end)

last_3_fruit = fruit[-3:]
# ['pear', 'lemon', 'watermelon']
print(last_3_fruit)

first_3_fruit = fruit[:3]
# ['apple', 'orange', 'banana']
print(first_3_fruit)

three_fruit_before_last = fruit[-4:-1]
# ['banana', 'pear', 'lemon']
print(three_fruit_before_last)

copy_of_string = fruit[:]
# ['apple', 'orange', 'banana', 'pear', 'lemon', 'watermelon']
print(copy_of_string)