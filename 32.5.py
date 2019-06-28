files = input().split()
 
print(list(map(lambda x: x.zfill(8) if (len(x)-x.index('.')>4) else x.zfill(7) ,files)))
