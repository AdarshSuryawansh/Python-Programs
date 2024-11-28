#Accept age from user
#age 0 to 18 print Child
#age 18 to 60 print Adult
#age 60 to 100 print Cinior citizen
#age above 100 print Invalid age

#Using AND operator

age = int(input("Enter a Age :"))
if(age > 0 and age <= 18):
    print("Child")
elif(age > 18 and age <=60):
    print("Adult")
elif(age > 60 and age <= 100):
    print("Cinior Citizen")
else:
    print("Invalid age !!!")