class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
     
    def __eq__(self,obj):
        if(self.x == obj.x and self.y == obj.y):#without creating object
            return (f"Equal")
        else:
            return ("Unequal")
        
    def __add__(self,obj):#with creating object
        c = Point()
        c.x = self.x+obj.x
        c.y = self.y+obj.y
        return c.x,c.y
        
p1 = Point(4,5)
p2 = Point(4,5)
#print(p1.x)
print(p1+p2)
print(p1.__add__(p2))
print("Both objects are:",p1==p2)
