
# Write the python program using reduce & lambda function to sum the values in to lists
from functools import reduce
l7 = [10,20,30,40,50,60]
output = reduce(lambda x,y:x+y,l7)
print(output)