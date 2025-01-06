#Q.Remove dublicate charactors from string.

s = "abcdabcdabcdbccadffgg"
lst = []
for i in s:
    if i not in lst:
        lst.append(i)

#print(lst)

s1 = "".join(lst)
print(s1)
