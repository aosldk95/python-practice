def fib(a):
    if a==1:
        return 1
    elif a==0:
        return 0
    return fib(a-1)+fib(a-2)


n = int(input())
print(fib(n))    
        
    
