a=int(input('시간당급여:'))
b=int(input('주당 총근무시간:'))
c=a*b
if b > 12:
    c=c*1.3
print('총급여:',c)
        
    
