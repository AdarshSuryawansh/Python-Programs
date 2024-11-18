#Q.Accept number from user and check weather even or odd.

num=int(input("Enter a Number :"))
r=num % 2
if(r == 0):
    print("odd number")
else:
    print("even number")