def AddDigits(List):
    sum = 0
    for j in List:
        #print(j)
        sum += int(j)
        #print(sum)
    return sum


st = input("Enter credit card number: ")
st = list(st)
n = len(st)
sum = 0
cardsum = 0

for i in range(n):
    st[i] = int(st[i])


for i in range(-2,-len(st)-1,-2):
    num = st[i]
    num *= 2
    if num > 9:
        st[i] = AddDigits(list(str(num)))
    else:
        st[i] = num   
 
cardsum = AddDigits(st)

if cardsum % 10 == 0:
    print("Valid")
else:
    print("Invalid")
