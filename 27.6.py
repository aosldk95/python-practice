with open('words.txt','r')as file:
    a=file.read()
    a=a.split()
    for i in range(len(a)):
        if 'c' in a[i]:
            a[i]=a[i].strip(',.')
            print(a[i])
