
#Removing spaces from the string
#rstrip() ==> removies the spaces from te right hand side.
#lstrip() ==> removes the spaces from the left hand side.
#strip()  ==>removes the spaces from the both side.

#rstrip
str = (input("Enter some string :")).rstrip()
if str == "sunny":
    print("Valid")
else:
    print("Invalid !!!")