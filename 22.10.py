a,b=map(int,input().split())
c=[]
for i in range(a ,b+1):
    c.append(2**i)
del c[1]
del c[-2]
print(c)
    
