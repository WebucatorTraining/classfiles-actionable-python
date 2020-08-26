def foo(f):
    print(f)
    def foo_inner():
        pass
    return foo_inner
    
def bar():
    pass

print(bar)
bar = foo(bar)
print(bar)