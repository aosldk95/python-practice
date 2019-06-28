s=int(input('성적을 입력하시오:'))
if s>=90:
    g='A'
elif 80<=s:
    g='B'
elif 70<=s:
    g='C'
else:
    g='F'
print('당신의 학점은',g,'입니다.')
