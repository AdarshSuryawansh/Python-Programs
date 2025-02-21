# Create A function ant take input from user and check even or odd.

user_input = int(input("Enter Some Number :"))
def CheckEvenOdd(num):
    if num % 2 == 0:
        print(f"{num} is a Even Number")
    else:
        print(f"{num} is a Odd Number")
#Call Function
CheckEvenOdd(user_input)