a=input()
a=a.split(' ')
b=0
for i in range(len(a)):
    a[i]=a[i].strip('.,')
    if a[i]=='the':
        b+=1
print(b)
