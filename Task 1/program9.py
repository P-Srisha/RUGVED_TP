st = input("Enter string to be encrypted: ")
n = int(input("Enter shift: "))

for i in st:
    if i.islower():
        if ord(i) >= 97 and ord(i) < 122-n:
            st = st.replace(i,chr(ord(i)+n))
        elif ord(i) > 122-n:
            shift = 122-ord(i)
            #temp1 = chr(ord(i)+shift)
            remshift = n - shift
            temp1 = chr(96+remshift)
            st = st.replace(i,temp1)

    elif i.isupper():
        if ord(i) >= 65 and ord(i) < 90-n:
            st = st.replace(i,chr(ord(i)+n))
        elif ord(i) > 90-n:
            shift = 90-ord(i)
            #temp1 = chr(ord(i)+shift)
            remshift = n - shift
            temp1 = chr(64+remshift)
            st = st.replace(i,temp1)
print("Caesar Cipher: ",st)