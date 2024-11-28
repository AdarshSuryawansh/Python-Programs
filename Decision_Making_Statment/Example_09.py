#Q.Accept marks for 3 subjects and calculate average.

sub1=int(input("Enter marks of sub1 :"))
sub2=int(input("Enter marks of sub2 :"))
sub3=int(input("Enter marks of sub3 :"))
avg=(sub1+sub2+sub3)/3
if(avg > 35 and avg <= 60):
    print("Grade C")
elif(avg > 60 and avg <= 74):
    print("Grade B")
elif(avg > 74 and avg <= 85):
    print("Grade A")
elif(avg > 85 and <= 100):
    print("Grade A+")
else:
    print("You are Fail !!!")