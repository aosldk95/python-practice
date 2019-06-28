a=int(input('정수:'))
max=a
loop=1
while loop<=4:
    a=int(input('정수:'))
    if a>max:
        max=a
    loop+=1
print('가장 큰 값:',max)
