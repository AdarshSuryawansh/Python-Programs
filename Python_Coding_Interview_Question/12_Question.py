
# Counting Vowel in a Given Word.

vowels = ['a','e','i','o','u']
word = "Programming"
count = 0
for cha in word:
    if cha in vowels:
        count += 1
print(count)