
# Write the python program using filter & lambda function to get the even numbers from list

l = [i for i in range(11)] #[0,1,2,3,4,5,6,7,8,9]
output = list(filter(lambda x:x%2==0,l))
print(output)