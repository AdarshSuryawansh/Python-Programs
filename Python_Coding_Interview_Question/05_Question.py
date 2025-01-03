

# Q.Write a python program to remove the duplicate from the string.

str_ = "mnmvnmvnmvn"

res = ""

for char in str_:
    if char not in res:
        res += char


print(res)