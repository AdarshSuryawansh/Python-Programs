
# Write the python program using filter & lambda function to filter out students with given condition
students = ['sunny','bunny','chinny','vinny','ashish','ganesh','ajit','vijay']
# get the student whose name ends with 'ny'
output = list(filter(lambda x:x.endswith('ny'),students))
print(output)