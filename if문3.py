s=int(input('성적을 입력하시요:'))
if 70<=s:
    print('통과하셨습니다.')
    if s>=90:
        print('A장학금')
    elif s>=80:
        print('B장학금')
elif s>=60:
    print('조건부 통과')
else:
    print('재수강')
print('ㅅㄱ')
