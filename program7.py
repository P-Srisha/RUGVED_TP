n = int(input("Enter number of terms of Fibonacci series: "))
a = 0
b = 1
c = 1
for i in range(n):
    if (i <= 1):
        print(i)
    else:
        c = a + b
        print(c)
        a = b
        b = c
