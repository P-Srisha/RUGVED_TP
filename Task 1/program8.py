st = input("Enter a string: ")
n = int(input("Enter number of letters in the substring: "))
List = []
if len(st)%n != 0:
    print("Cannot be divided into substrings")

for i in range(0,len(st),n):
    List.append(st[i:i+n])

equal = 1
for i in List:
    if List[0] != i:
        equal = 0
        break

if equal:
    for i in List:
        print(i, end = ' ')
else:
    print("Substrings are not same")
