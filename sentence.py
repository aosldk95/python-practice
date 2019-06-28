sentence='python is the\
most popular programming\
language in these days'
print(sentence)
#따옴표 세개를 사용하면 문장모양이 유지된다
greeting='hello world'
print(greeting[7])
print(greeting[0])
lang='python programming'
lang[1]
lang[1:3]
lang[1:6:2]
lang[:5]
lang[10::2]
a='hello';b='world'
c=a+b
print(c)
d=a+' '+b
print(d)
score=95
x='i got'+str(score)+'in the exam'
print(x)
a='hello'
a*3
len(a)
subject='programming'
'r'in subject
dir(str)
name='google'
name.upper()
'google'.upper()
name.lower()
a.isupper()
a.islower()
name.capitalize()
lang.title()
lang.istitle()
state='mississippi'
state.count('ssi')
state.count('s',5) #[5:]으로 잘라서 셈
state.count('s',1,5) #[1:5]범위
state.find('s')
state.find('i',5)#[5:]범위에서 'i'를 찾는다
friends=['alice','bob','cindy']
dash='-'
dash.join(friends)
lists='alice bob cindy david'
lists.split()
date='2016/12/25'
date.split('/')
