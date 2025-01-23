
# Counting consonantes in Given String

vowel = ['a','e','i','o','u']
word = "Programming"
count = 0
for cha in word:
    if cha not in vowel:
        count += 1
print(count)