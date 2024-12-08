
#Example 7: Python program to count the total number of digits in a number.

given_number = 123465789

# since we cannot iterate over an integer
# in python, we need to convert the
# integer into string first using the
# str() function

given_number = str(given_number)

count = 0
for i in given_number:
    count += 1
print(i)