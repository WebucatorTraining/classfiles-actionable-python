def all_true(iterable):
    # Return False if any item is False
    for item in iterable:
        if not item:
            return False
    # If we made it through the loop without returning False,
    #   then all items are True
    return True

def any_true(iterable):
    # Return True if any item is True
    for item in iterable:
        if item:
            return True
    # If we made it through the loop without returning True,
    #   then all items are False
    return False

def main():
    a = all_true([1, 0, 1, 1, 1])
    b = all_true([1, 1, 1, 1, 1])
    c = any_true([0, 0, 0, 1, 1])
    d = any_true([0, 0, 0, 0, 0])

    print(a, b, c, d) # Should be: False True True False

main()