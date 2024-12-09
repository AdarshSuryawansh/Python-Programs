
#Example 8: Python program to check if the given string is a palindrome.

given_string = "madam"

reverse_string = ""

for i in given_string:
    reverse_string = i + reverse_string

if(given_string == reverse_string):
    print(f"The String {given_string} is a palindrom")
else:
    print(f"The String {given_string} is Not a palindrom")