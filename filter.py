from functools import reduce

lst = [1,2,3,4,5,6,7,8,9]

def even(i):
    if(i%2==0):
        return i    
final_lst = list(filter(even,lst))


def sq(s):
    return s**2
mp = list(map(sq,final_lst))


def add(x,y):
    return x+y
rd = reduce(add, mp)


print("Original list:",lst)
print("\nFiltered even terms:",final_lst)
print("\nSquared even terms by mapping:",mp)
print(f"\nSumming using reduce: {rd}")
