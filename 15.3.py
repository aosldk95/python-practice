age = int(input())
balance = 9000
if 12>=age>=7:
    balance-=650
elif 13<=age<=18:
    balance-=1050
elif 19<=age:
    balance-=1250
print(balance)
