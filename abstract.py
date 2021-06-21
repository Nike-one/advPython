#Abstract

from abc import ABC, abstractmethod#importing ABC and abstractmethod from abc
 
class Polygon(ABC):
 
    @abstractmethod
    def noofsides(self):#created just a idea of noofsides don't have body just name
        pass
 
class Triangle(Polygon):
 
    # overriding abstract method
    def noofsides(self):#now making body
        print("I have 3 sides")
 
class Pentagon(Polygon):
 
    # overriding abstract method
    def noofsides(self):
        print("I have 5 sides")

R = Triangle()
R.noofsides()

R = Pentagon()
R.noofsides()
