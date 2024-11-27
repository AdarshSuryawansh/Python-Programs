#Q.Accept age from user
#age 0 to 18 print Child
#age 18 to 60 print Adult
#age 60 to 100 print Cinior citizen
#age above 100 print Invalid age

age=int(input("Enter Your Age :"))
if(age > 100):
    print("Invalid Age !!!")
elif(age >= 60):
    print("Cinior Citizen")
elif(age >= 18):
    print("Adult")
elif(age > 0):
    print("Child")
else:
    print("Invalid Age !!!")


