def fact(num):
    if num == 0:
        return 1
    else:
        return fact(num-1)*num 

n = int(input("Enter a number: "))
c = fact(n)
print("Factorial = ",c)