# Default Argument
# Some time we have  to define the default value to our positional argument such type of argument are called ass default argument.
# It will consider default value only when user does not pass any argument.

def wish(name = "Rajesh"):
    print(f"{name},Good Morning")
#call the function
wish("Adarsh")
wish() #Default argument