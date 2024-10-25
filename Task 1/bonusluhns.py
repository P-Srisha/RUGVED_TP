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
cardname = ''

if n == 15:
    if str(st[0:2]) == '34' or str(st[0:2]) == '37':
        cardname = 'American Express'
elif n == 13 and st[0] == '4':
    cardname = 'Visa'
elif n == 16:
    if st[0] == '4':
        cardname = "Visa"
    else:
        cardname = "Mastercard"

def Luhns(st):
    for i in range(n):
        st[i] = int(st[i])

    for i in range(-2,-n-1,-2):
        num = st[i]
        num *= 2
        if num > 9:
            st[i] = AddDigits(list(str(num)))
        else:
            st[i] = num
            
        
    cardsum = AddDigits(st)
    #print(st)
    #print(cardsum)
    if cardsum % 10 == 0:
        return True
    else:
        return False


if Luhns(st):
    print(cardname)
else:
    print("Invalid")