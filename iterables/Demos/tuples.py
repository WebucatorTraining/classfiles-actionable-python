def show_type(obj):
    print(type(obj))

# tuple created w/o parens (works but bad practice)
MAGENTA = 255, 0, 255
show_type(MAGENTA)

# When passing a tuple to a function, you need parens:
show_type((255, 0, 255))

# Passing the tuple w/o parens to a function will error
show_type(255, 0, 255)