with open('words.txt','r')as file:
    s=file.read()
    s=s.split()
    for i in range(len(s)):
        if s[i]==s[i][::-1]:
            print(s[i])
                

