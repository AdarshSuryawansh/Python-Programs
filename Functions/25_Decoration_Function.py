
def decor(func):
    def inner():
        print("Sending the person to the parlor")
        print("Display the colourful person")
    return inner

@decor
def display():
    print("Showing the person as it is")

display()
