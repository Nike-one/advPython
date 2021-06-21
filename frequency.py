d = {1:"Nikhil", 2:"OOPS concept", 3:"inheritance", 4:"Abstraction"}

def freq(w):
    dic = {}

    for i in w:
        c = w.count(i)
        dic[i] = c

    x = 0
    k = 0   
    m = max(dic.values())
    
    for key,val in dic.items():
        if val == m:
            x=val
            k = key
    return(k,x)



h_freq = dict(map(freq,d.values()))
print(h_freq)
