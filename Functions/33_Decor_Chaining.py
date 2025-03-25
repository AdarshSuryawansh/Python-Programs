
#Decor Chaining add,sub,multi,div

def decor1(func):
    def inner1(a,b):
        add_ = func(a,b)
        sub_ = a-b if a>b else b-a
        return add_,sub_
    return inner1

def decor2(func):
    def inner2(a,b):
        add_,sub_ = func(a,b)
        multi_ = a*b
        return add_,sub_,multi_
    return inner2

def decor3(func):
    def inner3(a,b):
        add_,sub_,multi_ = func(a,b )
        if a==b:
            return f"Cant't Devide With Zero"
        else:
            div_ = a/b
        return add_,sub_,multi_,div_
    return inner3

@decor3
@decor2
@decor1
def f1(a,b):
    return a + b

print(f1(10,2))