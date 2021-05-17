class Student:
    studentCount = 0
    markslst = []
    def __init__(self,name,phy,chem,maths):
        Student.studentCount += 1
        self.name = name
        self.phy = phy
        self.chem = chem
        self.maths = maths
        
        Student.markslst = [self.phy,self.chem,self.maths]
        
    def display(self):
        print("Name: ",self.name)
        print("Marks(phy,chem,maths)",Student.markslst,"\n")

s1 = Student("joe",45,48,42)
s2 = Student("mary",42,45,48)
s3 = Student("riya",34,45,42)

s1.display()
s2.display()
s3.display()
print("Number of Students: ",Student.studentCount)
