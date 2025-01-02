
# Q.Write the python program to check if two string are anagrams or not.

str1,str2 = input("Enter Two String with Space :").lower().split()

def check_anagram(s1,s2):
    if sorted(s1) == sorted(s2):
        print(f"{s1} and {s2} are Anagrams")
    else:
        print(f"{s1} and {s2} are Not Anagrams")

check_anagram(str1,str2)