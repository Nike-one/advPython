def square(fun):
    def inner(a,b):
        func_out = fun(a,b)
        return func_out**2
    return inner

@square
def add(x,y):
    return x+y

print("Square is:",add(2,8))

