# modify from Boon's code

import numpy as np

def matrandom(s):
    while True:
        matrix = np.random.uniform(low=0, high=9, size=(s, s))
        print("Im here")
        if np.linalg.det(matrix):
            break
    return np.around(matrix)


def pa(m):
    row = m.shape[0]  # row size of matrix m
    identity = np.eye(row)
    # permutation = np.random.permutation(identity)  # cannot use because in pivot position you can't found 0
    permutation = identity  # just be clear with var name
    temp = np.eye(row)  # for store the temp row matrix (it can't use the normal variable)
    for i in range(row):
        for j in range(i+1, row):
            if m[i][i] == 0:
                if m[j][i] != 0:  # search ไล่ในแต่ละ row แต่ col เดียวกันว่า ตน. ของ pivot มี row ไหนที่ != 0 เพื่อจะเอามาสลับ row
                    temp[0,:] = permutation[i, :]  # can access the content in the row by ex. at row 0, mat[0,:] which write in [] comma(,) followed by collon(:)
                    permutation[i, :] = permutation[j, :]
                    permutation[j, :] = temp[0,:]
                    break

    return permutation

def lu(pa):
    row = pa.shape[0]
    l = np.eye(row, dtype = np.double)
    u = pa  # ok, too
    # u = pa.astype(np.double)  # can use .copy(), both are copy matrix to var
    for i in range(row):
        for j in range(i+1, row):
            if u[i,i] != 0:
                factor = u[j, i] / u[i, i]
            else:
                factor = 0
            l[j, i] = factor
            for c in range(0, row):  # c คือไล่ไปแต่ละ col เพื่อลบทั้งบรรทัด (ทำ U)
                u[j, c] = u[j, c] - (factor * u[i, c])
    return l, u

# A = np.array([[0, 0, 9, 0], [0, 3, 3, 8], [8, 0, 5, 0],[2, 0, 0, 8]], dtype = np.double)
# A = np.array([[6, 0, 0, 0, 0], [0, 0, 5, 0, 7], [0, 5, 1, 2, 0], [3, 6, 0, 0, 0], [0, 0, 7, 0, 7]], dtype= np.double)
# A = np.array([[1,1,0], [4,6,1], [-2,2,0]])
A = np.array([[6,3], [5,2]])


print("\nA =\n", A)
P = pa(A)
# P = np.array([[0,0,1,0], [0,1,0,0], [1,0,0,0], [0,0,0,1]])
# P = np.eye(4)

print("\nP =\n", P)
print("\nPA =\n", P @ A)
(L,U) = lu(P @ A)
print("\nL =\n", L)
print("\nU =\n", U)
