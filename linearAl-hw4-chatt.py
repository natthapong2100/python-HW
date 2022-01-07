import numpy as np
def matelim(a):
    indent = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]], np.float32)

    #1
    div = a[0][0]
    for i in range(3):
        a[0][i] /= div
        indent[0][i] /= div
    #2
    for i in range(3):
        a[1][i] += (-1 * a[1][i]) * a[0][i]
        indent[1][i] = (-1 * indent[1][i]) * indent[0][i] + indent[1][i]
    #3
    for i in range(3):
        a[2][i] = (-1 * a[2][i]) * a[0][i] +  a[2][i]
        indent[2][i] = (-1 * indent[2][i]) * indent[0][i] + indent[2][i]
    #4
    div = a[1][1]
    for i in range(3):
        a[1][i] /= div
        indent[1][i] /= div
    #5
    for i in range(3):
        a[0][i] = (-1 * a[0][i]) * a[1][i] +  a[0][i]
        indent[0][i] = (-1 * indent[0][i]) * indent[1][i] +  indent[0][i]
    #6
    for i in range(3):
        a[2][i] = (-1 * a[2][i]) * a[1][i] +  a[2][i]
        indent[2][i] = (-1 * indent[2][i]) * indent[1][i] +  indent[2][i]
    #7
    div = a[2][2]
    for i in range(3):
        a[2][i] /= div
        indent[2][i] /= div
    #8
    for i in range(3):
        a[0][i] = (-1 * a[0][i]) * a[2][i] +  a[0][i]
        indent[0][i] = (-1 * indent[0][i]) * indent[2][i] +  indent[0][i]
    #9
    for i in range(3):
        a[1][i] = (-1 * a[1][i]) * a[2][i] +  a[1][i]
        indent[1][i] = (-1 * indent[1][i]) * indent[2][i] +  indent[1][i]
    return indent

def matrandom(n):
    C = np.random.randint(low=1, high=9, size=(n,n))
    return C

A = matrandom(3)

print('\nA = \n', A)
E = matelim(A)
print('\nE = \n', E)
print('\nEA = \n', np.around(E @ A, 3))