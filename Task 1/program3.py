# Hill number

n = int(input("Enter a number: "))
num = str(n)
mid = 0
hill = 0
for i in range(len(num)-1):
    if int(num[i]) > int(num[i+1]):
        mid = i
        hill = 1
        break
if mid != 0:
    for i in range(mid,len(num)-1):
        if int(num[i]) < int(num[i+1]):
            hill = 0
            break
elif mid == 0:
    print("NOT A HILL NUMBER")
    exit(0)
if hill == 0:
    print("NOT A HILL NUMBER")
else:
    print("HILL")