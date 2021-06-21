class fib:
    def __init__(self,n):
        self.a = 0
        self.b = 1
        self.n = n
        self.stop = 0

    def __iter__(self):
        return self

    def __next__(self):
        x = self.a
        if self.n > self.stop:
            self.a,self.b = self.b,self.a+self.b
            self.stop += 1
            return x
        else:
            raise StopIteration

    
for i in fib(10):
    print(i)
