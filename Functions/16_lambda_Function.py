
# Write a python program to find the biggest of two number using lamda function.

var = lambda x,y:x if x > y else y
x,y = [int(i)for i in input("Enter Two Numbers With Space :").split()]
print(f"The Biggest of {x} and {y} is :{var(x,y)}")