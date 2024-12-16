#Q.Write a python program to print the charactors and its positive index position in the list.

s = input("Enter some String: ")
z = 0
for i in s:
    print(f"The charactor,{i} is present in index {z}")
    z += 1