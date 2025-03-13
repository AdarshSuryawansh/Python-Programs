
# Write the python program using reduce & lambda function to find the sum of first 100 natural number

from functools import reduce
output = reduce(lambda x,y:x+y,range(1,101))
print(output)