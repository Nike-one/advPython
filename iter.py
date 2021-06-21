class myrange:
    def __init__(self,stp,st=0,inc=1):
        self.st = st
        self.stp = stp
        self.inc = inc

    def __iter__(self):
        return self

    def __next__(self):
        if self.st<self.stp:
            x = self.st
            self.st += self.inc
            return x
        else:
            raise StopIteration

for i in myrange(10,4,2):#if start and step is not provided it will take default start as 0 and increment by 1
    print(i)

