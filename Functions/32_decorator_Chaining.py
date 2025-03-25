
def decor1(func):
    def wrapper1():
        x = func()
        return x*2
    return wrapper1

def decor2(func):
    def wrapper2():
        y = func()
        return y**2
    return wrapper2


@decor2
@decor1
def f1():
    return 10

print(f1())