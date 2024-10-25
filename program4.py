# SELECTION SORT
s1 = input("Enter a string: ")
s2 = ''

while len(s1) != 0:
    small = 0
    for j in range(len(s1)):
        if s1[small] > s1[j]:
            small = j
    s2 += s1[small]
    s1 = s1.replace(s1[small], '', 1)
print(s1)
print("S2 = ", s2)