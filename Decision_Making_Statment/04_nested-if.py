#Nested-if:if inside another if

marks=int(input("Enter a Marks :"))
if(marks > 35 and marks <= 100):
    if(marks >= 60):
        print("First Class")
    else:
        print("Second Class")
else:
    print("Fail!!!")