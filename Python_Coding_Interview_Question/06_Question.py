
# Q.Write the python program to count of the number of occurance of chr in string output in
# in following way.
# eg. "ABCABC" ==> [[a,b], [b,2], [c,2]]

def count_char_occurrences(s):
    # Convert the string to lowercase to ensure case-insensitivity
    s = s.lower()

    # Create an empty dictionary to store the counts of each character
    count_dict = {}

    # Iterate through each character in the string
    for char in s:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1

    # Convert the dictionary to the desired list format
    result = [[char, count] for char, count in count_dict.items()]

    return result

# Test the function
s = "ABCABC"
output = count_char_occurrences(s)
print(output)
