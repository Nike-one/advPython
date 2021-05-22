#Instance Method

class Person:
    def __init__(self,name,sem):
        self.name = name
        self.sem = sem
    def myfunc(self):#instance method: we pass instatnce of a class (self) in myfunc as first argument
        print("Name as :",self.name)
        print("semester as:",str(self.sem)+"nd")

p1 = Person("Nikhil",2)
p1.myfunc()


#Class Method

class Person:
    age = 18
    @classmethod #class method created ie, reference of class is created so no need to create object to execute it
    def printAge(cls):
        print("AGE:",cls.age)

Person.printAge()

#Static Method
''' static method: cannot access or modify
    class or object state has its own argument
    or no aurgument'''
class Person:
    @staticmethod
    def static(n):

        print("This in staic method",n)

Person.static(1)
 
