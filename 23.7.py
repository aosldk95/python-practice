a,b=map(int,input().split())
c= []
for i in range(b):
    c.append(list(input()))
for i in range(b):
    for j in range(a):
        if c[i][j]=='*':
            continue
        else:
            c[i][j]=0
            for y in range(i-1,i+2):
                for x in range(j-1,j+2):
                    if y<0 or x<0 or y>=b or x>=a:
                        continue
                    elif c[y][x]=='*':
                        c[i][j]+=1
from pprint import pprint
pprint(c, width=15/2*a)
                

