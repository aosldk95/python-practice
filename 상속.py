class Shape:
    
    def _init_(self):
        self.x=0
        self.y=0
        
    def draw(self):
        pass
    
    def getarea(self):
        print('getarea')
        
class Circle(Shape):
    
    def _init_(self):
        self.r=0
        
    def getarea(self):
        return 2 * 3.14 * self.r * self.r    

shape=Shape()
shape.getarea()

class Ract(Shape):
    def _init_(self):
        self.w=0
        self.h=0
    
    def getarea(self):
        return self.w*self.h

c=Circle()
c.r=2
print(c.getarea())

r= Ract()
r.w=3
r.h=4
print(r.getarea())

