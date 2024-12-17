#Q.Write a python program to print the charactors and its negative index position in the list.

s = input("Enter some String: ")
i = 0
for chr in s:
    print("The charactor is",chr,"its negative index is",i-len(s))
    i += 1


