mat = [[1,2],[3,4],[5,6]]
trans = [[r[i] for r in mat] for i in range(len(mat[0]))]
print(trans,"\n")

m1 = [1,2,3]
m2 = [4,5,6]
matr = [m1[i]*m2[i] for i in range(len(m1))]
print("Multiplying Matrix",matr,"\n")

mtx = [[r*c for r in m2] for c in m1]
print("Multiplying each element of m2 in m1[0],m[1],m1[2]....\n",mtx)
