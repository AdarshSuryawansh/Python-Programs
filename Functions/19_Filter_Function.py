
# Write the python program using filter & lambda function to get the numbers which are divisible by 3 and odds.

l3 = [i for i in range(11)]
output = list(filter(lambda x:x%3==0 and x%2!=0,l3))
print(output)