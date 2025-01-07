#Q.Take string from user and determine its type

ur_input = input("Enter User Input :")

if ur_input.isalnum():
    if ur_input.isalpha():
        print("It is Charactor Only")
    elif ur_input.isdigit():
        print("It is Digit Only")
    else:
        print("It is Combination Of Caharctor and Digit")
elif ur_input.isspace():
    print("It is space Charactor")
else:
    print("It is Special Charactor")