"""class A:
    foo = 1
    bar = 1
    def __init__(self):
        self.foo = 2
    
a = A()
print(a.foo, A.foo, a.bar, A.bar)"""

# Modify mutable object stored as a class attribute

"""class A:
    foo = ['a','b','c']
    def __init__(self):
        self.foo.append('d')
    
a = A()
print(a.foo, A.foo)"""

# Class method

class A:
    foo = 1
    @classmethod
    def my_class_method(cls):
        cls.foo += 1
        return cls.foo

x = A.my_class_method()

a = A()
y = a.my_class_method()

print(x, y)