

def decor(func):
    def inner(name):
        if name in ["PM","CM","Minister"]:
            print("Hello SIr Yoy are very importnt for us..!")
            print("Hello sir very good morning")
        else:
            func(name)
    return inner

@decor
def wish(name):
    print(f"hello {name} Good Morning...!!")

wish("Sunny")
wish("PM")