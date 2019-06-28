a=input().split(';')
a=list(map(int,a))
a.sort(reverse=True)
for i in range(len(a)):
    a[i]='%9s'%format(a[i],',')
print(a)
