class Person:
    def __init__(self,name,sem):
        self.name = name
        self.sem = sem
    def myfunc(self):#instance method: we pass instatnce of a class (self) in myfunc as first argument
        print("Name as :",self.name)
        print("semester as:",str(self.sem)+"nd")

p1 = Person("Nikhil",2)
p1.myfunc()
