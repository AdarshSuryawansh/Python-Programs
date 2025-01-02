
# Python Coding Interview Question

# 1.Write the python program to swap the case of the string

str_ = "AbcD"
res =""

for char in str_:
    if char.isupper():
        res += char.lower()
    elif char.islower():
        res += char.upper()
    else:
        res += char


print(res)

