# Simple sort() method
colors = ['red', 'blue', 'green', 'orange']
# colors.sort()
new_colors = sorted(colors) # This one has been done for you
print(new_colors)

# The reverse argument:
colors.sort(reverse=True)
print(colors)

# The key argument:
colors.sort(key=len)
print(colors)

# The key argument with named function:
def get_lastname(name):
    return name.split()[-1]

people = ['George Washington', 'John Adams',
          'Thomas Jefferson', 'John Quincy Adams']
people.sort(key=get_lastname)
print(people)

# The key argument with lambda:
people.sort(key=lambda name: name.split()[-1])
print(people)

# Combing key and reverse
colors.sort(key=len, reverse=True)
print(colors)