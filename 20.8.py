a,b=map(int,input().split())
for i in range(a,b+1):
    if i%5==0 and i%7==0:
        print('FizzBuzz')
    elif i%7==0:
        print('Buzz')
    elif i%5==0:
        print('Fizz')
    else:
        print(i)
