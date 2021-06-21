class rev:
    def __init__(self,l):
        self.l = l
        self.st = 0
        
    def __iter__(self):
        return self

    def __next__(self):
        
        while(self.st<len(self.l)):
            self.st-=1
            return(self.l[self.st])
            
lst = [1,2,3,4,5,6]

r = rev(lst)

for i in range(len(lst)):
    print(next(r))
