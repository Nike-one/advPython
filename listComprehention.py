lst = [i**2 for i in range(1,6)]
print("Square:",lst)

#if-else in list Comprehension(using filter condition)

l = [i for i in lst if i%2==0]
print("Even:",l)

obj = [f"Even: {i}" if i%2==0 else f"Odd: {i}" for i in lst]
print("even odd list comprehension\n",obj)


