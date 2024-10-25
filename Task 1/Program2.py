s = input("Enter a string: ")
s = list(s)
s.sort()
st = ''
for i in s:
    st += i

print(st)

for i in set(s):
    print(i ,":",s.count(i))