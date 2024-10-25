# PROGRAM 6

s1 = input("Enter string 1: ")
s2 = input("Enter string 2: ")
def Anagrams(s1,s2):
    a = 1
    if len(s1) == len(s2):
        for i in s1:
            if i not in s2:
                a = 0
                break
    return a
result = Anagrams(s1,s2)
if result == 0:
    print("Not anagrams")
else:
    print("Anagrams")