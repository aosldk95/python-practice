class person:
    def __init__(self ,name,age,address):
        self.hello='안녕하세요'
        self.name=name
        self.age=age
        self.address=address
    def greeting(self):
        print('{0} 저는 {1}입니다. '.format(self.hello,self.name))
james=person('제임스',20,'서울시 서초구 반포동')
james.greeting()
print('이름:',james.name)
print('나이:',james.age)
print('주소:',james.address)
