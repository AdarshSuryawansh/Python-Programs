# Variable-length_Argument
# Sometime we have to pass variable number of argument to out function such a type of argument is called as veriable lenght.
# We have declare such argument using * symbol as follows :
 # def f1(*n):
  #    pass
# We can call such function by using any number of argument includig zero only
# Internaly all these argument are represent as a form of tuple

# Create  afunction to compute the sum of number
def add(*n):
    result = 0
    for i in n:
        result += i
    print("The Sum :",result)
#call the function
add()
add(10,20)
add(10,20,30,40,50)