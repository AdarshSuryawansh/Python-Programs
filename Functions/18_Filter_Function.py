
# Write the python program using filter & lambda function to get the odd numbers from list

l2 = [i for i in range(11)]
output = list(filter(lambda x:x%2!=0,l2))
print(output)