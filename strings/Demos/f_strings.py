import math
user_name = input("What is your name? ")

# Concatenation:
greeting = "Hello, " + user_name + "!"

# The format() method:
greeting = "Hello, {}!".format(user_name)

# f-string:
greeting = f"Hello, {user_name}!"
print(greeting)

# format specification is also available:
pi_statement = f"pi is {math.pi:.4f}"
print(pi_statement)