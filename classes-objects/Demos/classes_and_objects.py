print('Test: "Hello"')
print(type('Hello'), isinstance('Hello', str))
print('-'*70)

print('Test: 1')
print(type(1), isinstance(1, int))
print('-'*70)

print('Test: [\'a\',\'b\',\'c\']')
print(type(['a','b','c']), isinstance(['a','b','c'], list))
print('-'*70)

print('Test: (1,2,3)')
print(type((1,2,3)), isinstance((1,2,3), tuple))
print('-'*70)

print("Test: {'a':1, 'b':2}")
print(type({'a':1, 'b':2}), isinstance({'a':1, 'b':2}, dict))
print('-'*70)

print("Test: print")
print(type(print))
print('-'*70)

print("Test: age=range(0,100) range")
age = range(0,100)
print(type(age), type(range))
print('-'*70)

print("Test object from user created class")
class Player:
    pass

serena = Player()

print(type(serena), type(Player), isinstance(serena, Player))
print('-'*70)

print("Test object from user created class with __init__ method")
class Player2:
    def __init__(self, name):
        self.name = name

serena = Player2('Serena Williams')

print('Hello,', serena.name + '!')