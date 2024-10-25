def triple_and(a,b,c):
    if (a*b*c != 0):
        return True
    else:
        return False

a = int(input("Enter parameter 1: "))
b = int(input("Enter parameter 2: "))
c = int(input("Enter parameter 3: "))

print(triple_and(a,b,c))