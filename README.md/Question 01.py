
# Question 1: Handling Division by Zero

# writr a function that takes two integers as input and returns there division.Use try,except,and
# finally block to handle division by zero and print an approprite masssage

try:
    x = int(input("Enter x value: "))
    y = int(input("Enter y value: "))
    res = x/y
except(ZeroDivisionError,ValueError) as e:
    print("Please provide valid value becoz:",e)
else:
    print(f"The division of {x} and {y} is {res}")