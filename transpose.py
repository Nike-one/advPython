mtx = [[10,20,30],[40,50,60],[70,80,90]]
row = len(mtx)
col = len(mtx[0])
trans = []

print("Matrix:")
for i in mtx:
    print(i)
print()

for i in range(0,row):
    r = []
    for ro in mtx:
        r.append(ro[i])
    trans.append(r)

print("transpose of Matrix:")
for i in trans:
    print(i)
print()
