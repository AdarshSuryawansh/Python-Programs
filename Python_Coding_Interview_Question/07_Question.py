
# Q Write the python program to reverse the given number
# eg. -120 to - -21

def reverse_number(n):
    # Check if the number is negative
    is_negative = n < 0

    # Convert the number to a string, remove the negative sign if present
    n_str = str(abs(n))

    # Reverse the string
    reversed_str = n_str[::-1]

    # Convert the reversed string back to an integer
    reversed_num = int(reversed_str)

    # If the original number was negative, add the negative sign back
    if is_negative:
        reversed_num = -reversed_num

    return reversed_num

# Test the function
num = -120
output = reverse_number(num)
print(output)
