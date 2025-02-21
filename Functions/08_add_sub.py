# Returning the multipla values from function.

# Create function to perform add and sub operation

def add_sub(a,b):
    sum = a + b
    sub = a - b
    return sum,sub
#Call the function
out1,out2 = add_sub(15,10)
print("Addition is :",out1)
print("Substaction is :",out2)