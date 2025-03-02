
# Variable-Length keyword Argumnent

def f1(**kwarug):
    for k,w in kwarug.items():
        print(k,"=",w)
#Call the function
f1(n1=12,n2=20,n3=45)
f1(rollno=20,name="Adarsh",marks=99,subject="python Programing")