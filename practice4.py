a=int(input('양의 정수를 입력하시오: '))
b=1
d=0
while b<=a:
    if a%b==0:
        d+=1
        print(b)
    b+=1
print('약수의 개수:',d)
