class A:
    def __init__(self, name):
        self.name = name
        
    def intro(self):
        print('Hello, my name is {}.'.format(self.name))
    
    def outro(self):
        print('Goodbye!')

class B(A):
    def intro(self):
        print('Hi, I am {}.'.format(self.name))

a = A('George')
b = B('Ringo')

a.intro()
b.intro()
a.outro()
b.outro()