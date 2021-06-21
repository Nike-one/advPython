class A:
    def __init__(self):
        self.__a = 10

    def show(self):
        print("Private Var:",self.__a)

a = A()
#print(a.__a) #get error
a.__a = 20 #new variable created named __a which is printed in next line
print(a.__a)
print("private variabe (Mangaled name):",a._A__a)#accessing private variabe which is named as _className__privateVar
a.show() #callig private variable through show method
