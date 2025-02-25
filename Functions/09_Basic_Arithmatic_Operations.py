# Create a function to perform a basic arathmatic operators.

#Create the function
def calc(a,b):
    sum = a + b
    sub = a - b
    multi = a * b
    div = a / b
    return sum,sub,multi,div
#Call the function
out1, out2, out3, out4 = calc(10,5)
print("Addition is :",out1)
print("Substraction is :",out2)
print("Multiplaction is :",out3)
print("Division is :",out4)