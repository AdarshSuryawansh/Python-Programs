
# Python Coding Interview Question

# 2.Write the python program to swap the case of the string

user_input = input("Enter Some String :")

def swap_case(str_):
    res = ""
    for char in str_:
        if char.isupper():
            res += char.lower()
        elif char.islower():
            res += char.upper()
        else:
            res += char
    return res

output = swap_case(user_input)
print(f"String after swaping :",output)
