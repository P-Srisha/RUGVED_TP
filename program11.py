st = input("Enter the text (Don't use periods whenever not needed or double spaces): \n")
stcpy1 = st
stcpy2 = st
charcount, wordcount, sencount = 0,0,0
for i in st:
    if i.islower() or i.isupper():
        charcount += 1
stcpy1 = stcpy1.split()
for i in stcpy1:
    wordcount += 1
stcpy2 = stcpy2.split('.')
for i in stcpy2:
    sencount += 1

if sencount != 1:
    sencount -= 1

awl = (charcount/wordcount)
r = (sencount/wordcount)

coleman_value = 5.88*awl + 29.6*r - 15.8
#print(awl,r)
#print(charcount,wordcount,sencount)
print(coleman_value)

coleman_value = int(coleman_value)

print(coleman_value)

if coleman_value <= 5:
    print("5th grade or below: Very easy to read")
elif coleman_value == 6:
    print("6th grade: Easy to read")
elif coleman_value == 7:
    print("7th grade: Quite easy to read")
elif coleman_value <= 10:
    print("8th, 9th, 10th grade: Conversational English")
elif coleman_value <= 12:
    print("11th, 12th grade: Quite hard to read")
elif coleman_value <= 16:
    print("College: Not easy to read- difficult")
else:
    print("Very hard to read")