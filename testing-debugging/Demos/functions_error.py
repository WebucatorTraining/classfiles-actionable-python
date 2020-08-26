def prepend(s, c):
    return c + s

def append(s, c):
    return s + c

def insert(s, c, pos):
    return s[0:pos] + c + s[pos:-1] # wrong