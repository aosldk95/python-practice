a,b=map(int,input().split())
c=[]
for i in range(a ,b+1):
    c.insert(len(c),2**i)
del c[1]
del c[-2]
print(c)
    
