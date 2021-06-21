from functools import reduce

lst = [1,2,3,4,5,6,7,8,9]

even = list(filter(lambda x : x%2==0,lst))
sq = list(map(lambda y : y**2,even))
add = reduce(lambda a,b : a+b,sq)

print(f'''original list: {lst}
even of list: {even}
square of even: {sq}
add of square: {add}''')
