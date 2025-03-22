
#Decorator Chaining
#How we call the function with and without decorator.

def decor(func):
    def inner(name):
        if name == "Sunny":
            print("#"*50)
            print("Hello Sunny Very Good Morning")
            print("#"*50)
        else:
            func(name)
    return inner


def wish(name):
    print(f"Hello {name} Good Morning..")

decorrted_wish = decor(wish)

decorrted_wish("Bunny")
decorrted_wish("Sunny")

wish("Bunny")
wish("Sunny")