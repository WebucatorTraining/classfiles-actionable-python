# ZeroDivisionError
try:
    1/0
except Exception as e:
    print(type(e))
    print(e, '\n')

# ValueError
try:
    int('a')
except Exception as e:
    print(type(e))
    print(e, '\n')

# NameError
try:
    print(foo)
except Exception as e:
    print(type(e))
    print(e, '\n')

# FileNotFoundError
try:
    open('non-existing-file.txt', 'r')
except Exception as e:
    print(type(e))
    print(e, '\n')

# ImportError
try:
    import non_existing_module
except Exception as e:
    print(type(e))
    print(e, '\n')

# TypeError
try:
    nums = [1, 2] # Lists are iterables, not iterators
    next(nums)
except Exception as e:
    print(type(e))
    print(e, '\n')

# AttributeError
try:
    greeting = 'Hello'
    greeting.print() # strings don't have a print() method
except Exception as e:
    print(type(e))
    print(e, '\n')

# StopIteration
try:
    nums = [1, 2]
    iter_nums = iter(nums)
    print(next(iter_nums))
    print(next(iter_nums))
    print(next(iter_nums))
except Exception as e:
    print(type(e))
    print(e, '\n')

# KeyError
try:
    grades = {'English':97, 'Math':93, 'Art':74, 'Music':86}
    print(grades['Science'])
except Exception as e:
    print(type(e))
    print(e, '\n')