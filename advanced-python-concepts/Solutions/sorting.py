# Simple sort() method
colors = ['red', 'blue', 'green', 'orange']
# colors.sort()
new_colors = sorted(colors) # This one has been done for you
print(new_colors)

# The reverse argument:
# colors.sort(reverse=True)
# print(colors)
new_colors = sorted(colors, reverse=True)
print(new_colors)

# The key argument:
# colors.sort(key=len)
# print(colors)
new_colors = sorted(colors, key=len)
print(new_colors)

# The key argument with named function:
def get_lastname(name):
    return name.split()[-1]

people = ['George Washington', 'John Adams', 
          'Thomas Jefferson', 'John Quincy Adams']
# people.sort(key=get_lastname)
# print(people)
new_people = sorted(people, key=get_lastname)
print(new_people)

# The key argument with lambda function:
people = ['George Washington', 'John Adams', 
          'Thomas Jefferson', 'John Quincy Adams']
# people.sort(key=lambda name: name.split()[-1])
# print(people)
new_people = sorted(people, key=lambda name: name.split()[-1])
print(new_people)

# Combining key and reverse
# colors.sort(key=len, reverse=True)
# print(colors)
new_colors = sorted(colors, key=len, reverse=True)
print(new_colors)