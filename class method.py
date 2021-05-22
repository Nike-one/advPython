
class Person:
    age = 18
    @classmethod #class method created ie, reference of class is created so no need to create object to execute it
    def printAge(cls):
        print("AGE:",cls.age)

Person.printAge()
