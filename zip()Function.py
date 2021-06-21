key = [1,2,3,4]
val = ["a","b","c","d"]
d = {key:value for key,value in zip(key,val)}#zip returns tuple of 2 or more list in key value pair
print(d)
