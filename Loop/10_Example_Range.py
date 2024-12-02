#Q Accept num from user calculate and display factorial of a given number.

num = int(input("Enter a Number :"))
fact = 1
for i in range(1,num+1):
    fact = fact * i
print("Factorial of",num,"is :",fact)