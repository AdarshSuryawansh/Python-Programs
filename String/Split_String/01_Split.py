#Spliting String
#split() ==> Default sepreator for the split is space and we can assing any other char also.And the default return type of list only.

s = "Learning python is very easy"
print(s.split())

s1 = "27-11-2024"
res = s1.split("-") #List
for i in res:
    print(i)