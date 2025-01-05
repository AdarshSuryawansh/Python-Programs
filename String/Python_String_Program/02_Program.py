#Q.take a user name or password from user and grant the access accoring that.remember username is case sensitive
# where as a password should be case sensitive.

us_name = input("Enter User Name :").lower()
pass_ = input("Enter Password :")
if us_name == "gamaka" and pass_ == "Gamaka@1234":
    print("Access granted")
else:
    print("Access denied !!!")