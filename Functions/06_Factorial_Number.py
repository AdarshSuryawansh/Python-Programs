#Create a function and take a input from user and find the factorial of given number.

user_input = int(input("Enter Some Number :"))
def fact(num):
    result = 1
    while num >= 1:
        result *= num
        num -= 1
    return result
#Call Fubction
output = fact(user_input)
print(output)
