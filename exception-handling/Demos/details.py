try:
    1/0
except Exception as e:
    print(type(e)) # prints exception type
    print(e) # prints friendly message