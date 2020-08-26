class A:
    def __init__(self, name):
        self.name = name
        
    def intro(self):
        print('Hello, my name is {}.'.format(self.name))
    
    def outro(self):
        print('Goodbye!')

class B(A):
    def intro(self):
        super().intro()
        print('It\'s very nice to meet you.')

a = A('George')
b = B('Ringo')

a.intro()
print('-------')
b.intro()
print('-------')
a.outro()
b.outro()