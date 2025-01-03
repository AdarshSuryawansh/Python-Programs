
# Q.Write the python program to check if two string are palindrom or not

s = input("Enter Some String :").lower()

if s == s[::-1]:
    print("String is Palindrom..!")
else:
    print("String is Not Palindrom..1")