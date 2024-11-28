# Q.Accept 3 numbers from user print largest number among them.

num1=int(input("Enter num1 :"))
num2=int(input("Enter num2 :"))
num3=int(input("Enter num3 :"))
if(num1 >= num2 and num1 >= num3):
    print("Largest number is num1")
elif(num2 >= num1 and num2 >= num3):
    print("Largest number is num2")
else:
    print("Largest number is num3")