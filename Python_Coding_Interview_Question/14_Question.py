# Counting the number of occurrence of a caharactor in a string

word = "Python"
charactor = "P"
count = 0
for letter in word:
    if letter == charactor:
        count +=1
print(count)