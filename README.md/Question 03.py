
# Question 03: Handling Multiple Exceptions

# Write a function that takes a list of integers and returns their sum.Use try,except,and finally
# block to handle TypeError if a non-integer value is encountered and print an approprote massage.

def returSum(l):
    try:
        res = sum(l)
    except TypeError:
        print("Please add only numbers")
    else:
        print("The Sum:",res)

ur_input = evel(input("Enter List of Numbers: "))

returnSum(ur_input)