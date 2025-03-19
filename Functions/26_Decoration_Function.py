
def decor(func):
    def inner(a,b):
        print("#"*50)
        print("The Sum :",func(a,b))
        print("#"*50)
    return inner

@decor
def add(a,b):
    return a + b

print(add(30,40))