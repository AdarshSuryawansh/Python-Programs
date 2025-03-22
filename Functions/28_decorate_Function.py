
def decor(func):
    def wrapper(a,b):
        if b == 0:
            print("Hello stupid how can we divide with zero..?")
        else:
            print(func(a,b))
    return wrapper

@decor
def div(a,b):
    return a/b

div(10,5)
div(10,0)