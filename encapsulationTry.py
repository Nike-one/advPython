class hello:
    def __init__(self):
        self.__a = 4
        
    def display(self):#getters
        return("s:", self.__a)

    def change(self,n):#setters
        self.__a = n

h = hello()
print("Before:")
print(h.display())
h.change(15)
print("After:")
print(h.display())





































h.display()
h.change(4)
h.display()
#print(h.a)#raise error


