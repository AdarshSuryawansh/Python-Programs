#Accept a charactor  from user and check weather it is vowel or consonant using in operator.

ch = input("Enter a single Charactore :")
if(ch in('a','e','i','o','u','A','E','I','O','U')):
    print("It is Vowel")
else:
    print("It is Consonent")