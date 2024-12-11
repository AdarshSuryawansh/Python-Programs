
# Example 12: Python program that accepts a string and calculates the number of digits and letters.

user_input = input("Enter any String :")
digits = 0
letters = 0
for i in user_input:
    if i.isdigit():
        digits = digits + 1
    elif i.isalpha():
        letters = letters + 1
print(f"The Userinput {user_input} Digits are {digits} and letters are {letters}")