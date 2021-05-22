''' static method: cannot access or modify
    class or object state has its own argument
    or no aurgument'''
class Person:
    @staticmethod
    def static(n):

        print("This in staic method",n)

Person.static(1)
 
