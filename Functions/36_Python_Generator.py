
# Create the generator function to print the fibonacci number
# next number is the sum of privious two number
# 0,1,1,2,3,5,8,

def fibo():
    a,b = 0,1
    while True:
        yield a
        a,b = b,a+b

g = fibo()

for i in g:
    if i > 100:
         break
    print(i)