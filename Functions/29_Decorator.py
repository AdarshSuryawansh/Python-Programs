
def add_sub(func):
    def wrapper(a,b):
        add_ = func(a,b)
        sub_ = a - b if a > b else b - a
        return add_,sub_
    return wrapper

@add_sub
def calc(a,b):
    return a + b

print(calc(10,30))