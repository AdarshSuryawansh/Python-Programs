
# Writing Fibonacci series

n = int(input("Enter a Number :"))
x = 0
y = 1
z = 0
while(z <= n):
    print(z)
    x = y
    y = z
    z = x+y