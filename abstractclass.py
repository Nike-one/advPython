#Abstract Class

from abc import ABC,abstractmethod

class Poly(ABC):
    #we never define a constructor __init__ in abstract we use abstract method
    @abstractmethod
    def area(self):
        pass
    def show(self):
        print("this is Poly class")

class Rect(Poly):
    def __init__(self,l,b):
        self.l = l
        self.b = b
    def area(self):
        print("area =",self.l*self.b)

r1 = Rect(5,9)
r1.area()
