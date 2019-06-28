a=int(input())
for i in range(1,2*a,2):
    for j in reversed(range(a)):
        if j>((i-1)/2):
            print(' ',end='')
    for j in range(1,a*2):
        if i>=j:
            print('*',end='')
        else:
            print(' ',end='')
    print()
            
            
