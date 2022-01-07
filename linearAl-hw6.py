import numpy as np

def matrandom(val):
    if val > 10 or val < 1:
        print("The max number is 10 and min is 0, please choose new number.\n")
        return None
    Matrix = np.random.uniform(low=0, high=9, size=(val,val))
    while( 0 == np.linalg.det(Matrix)):
        Matrix = np.random.uniform(low=0, high=9, size=(val,val))
    return Matrix

def pa(Matrix):
    size = Matrix.shape[0]
    P = np.eye(size)
    if np.linalg.det(P) == 0:
        print("Matrix is not invertible.")
        return None
    if size == 1:
        return np.array([[1]])
    (rows, columns) = P.shape  # 4, 4
    for i in range(columns):
        for j in range(i,rows):
            if Matrix[j,i] != 0:
                if j == i:
                    break
                P[[i,j]] = P[[j,i]]
                Matrix = Matrix@P
                break

    return P

def lu(PAmatrix):
    n=PAmatrix.shape[0]
    L = np.eye(n, dtype = np.double)
    U = PAmatrix.copy()
    Matrix = PAmatrix.copy()
    for k in range(0,n):
        for r in range(0,n):
            if (k<r):
                factor = (PAmatrix[r,k]/PAmatrix[k,k])
                L[r, k] = factor
                for c in range(0,n):
                    PAmatrix[r,c] = PAmatrix[r,c] - (factor * PAmatrix[k,c])
                    U[r,c] = PAmatrix[r,c]
    for i in range(n):
        for j in range(n):
            if (np.isclose(U[i,j],0.0) and i != j):
                U[i,j] = 0
            elif (np.isclose(L[i,j],0.0) and L[i,j] != 1):
                L[i,j] = 0

    return L, U


A = np.array([[0, 0, 9, 0], [0, 3, 3, 8], [8, 0, 5, 0], [2, 0, 0, 8]])
# A = np.array([[6, 0, 0, 0, 0], [0, 0, 5, 0, 7], [0, 5, 1, 2, 0], [3, 6, 0, 0, 0], [0, 0, 7, 0, 7]])

print("\nA =\n", A)
P = pa(A)
print("\nP =\n", P)
print("\nPA =\n", P @ A)
(L, U) = lu(P @ A)
print("\nL =\n", L)
print("\nU =\n", U)