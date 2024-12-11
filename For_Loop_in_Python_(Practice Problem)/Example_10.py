
# Example 10: Python program to count the number of even and odd numbers from a series of numbers.

num_lst = [12,22,16,18,16,4,20,6,71,22,345]

for i in num_lst:
    if i % 2 == 0:
        print(f"{i} = It is a Even Number")
    else:
        print(f"{i} = It is a Odd Number")