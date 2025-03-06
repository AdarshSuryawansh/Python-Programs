# Write the python program to find the sum of two number using lamda function

sum_ = lambda a,b:a + b
a,b = [int(i)for i in input("Enter Two Numbers With Space :").split()]
print(f"The Addition of {a} and {b} is :{sum_(a,b)}")