
# Example 13: Python program to convert the month name to a number of days.


month = ["January", "April", "August","June","Dovember"]

# iterate through each mont in the list
for i in month:
    if i == "February":
            print("The month of February has 28/29 days")
    elif i in ("April", "June", "September", "November"):
            print("The month of",i,"has 30 days.")
    elif i in ("January", "March", "May", "July", "August", "October", "December"):
            print("The month of",i,"has 31 days.")
    else:
            print(i,"is not a valid month name.")