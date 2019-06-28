class pizabase:
    def getprice(self):
        return 0

class itemgroup(pizabase):
    def __init__(self):
        self.items = []


    def getprice(self):
        sum=0
        for i in range( len(self.items) ):
            sum=sum+self.items[i].getprice()
        return sum

class doughA(pizabase):
    def getprice(self):
        return 100

class doughB(pizabase):
    def getprice(self):
        return 200

class toppingA(pizabase):
    def getprice(self):
        return 10

class toppingB(pizabase):
    def getprice(self):
        return 20

def createtoppingsetA():
    p=itemgroup()
    p.items.append(toppingA())
    p.items.append(toppingB())
    return p

def createspecialpizza():
    p=itemgroup()
    p.items.append(doughA())
    p.items.append(createtoppingsetA())
    return p

def creategoldpizza():
    p=itemgroup()
    p.items.append(doughA())
    p.items.append(toppingA())
    return p

pizza=creategoldpizza()
print(pizza.getprice())