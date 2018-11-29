class circle:
    __PI = 3.141
    def __init__(self,r):
        self.radius = r
    def area(self):
        return (self.__PI*self.radius*self.radius)
    def circumf(self):
        return (2*3.141*self.radius)
    def __str__(self):
        return "this is circle"
class rectangle:
    def __init__(self,l,b):
        self.length = l
        self.breadth = b
    def area(self):
        return (self.length*self.breadth)
    def circumf(self):
        return (2*(self.length+self.breadth))
c1 = circle(10)
c2 = circle(20)
print c1
print c1.area()
print c1.circumf()
print c1._circle__PI
print c2.area()
print c2.circumf()
R1 = rectangle(10,20)
print R1.area()
print R1.circumf()




    