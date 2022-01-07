from sympy.matrices import Matrix, eye, zeros, ones, diag
from sympy import *


def completeSol(Ax, bx):
    Ax_shape = list(Ax.shape)
    rows = Ax_shape[0]
    cols = Ax_shape[1]
    Ax_result = Ax.col_insert(cols + 1, bx)
    Ax_result, pivot_cols = Ax_result.rref()
    augmented = Ax_result.col(-1)
    index = 0
    xp = Matrix(cols, 1, range(cols))
    fc = []
    for i in range(0, cols):
        if (i in pivot_cols):
            xp[i, 0] = augmented[index]
            index += 1
        else:
            xp[i, 0] = 0
            fc.append(i + 1)
    Ax_result.col_del(-1)

    blank_cols = zeros(1, cols)  # Check zero rows

    xs = zeros(cols, len(fc))
    while (Ax_result.row(-1) == blank_cols):
        Ax_result.row_del(-1)

    for i in range(len(fc)):
        xs[fc[i] - 1, i] = 1
    for i in range(len(fc)):
        for j in range(Ax_result.rows):
            xs[pivot_cols[j], i] = Ax_result[j, fc[i] - 1] * (-1)
    return xp, xs, fc


# A = Matrix([[1,3,1,2],[2,6,4,8],[0,0,2,4]])
# A = Matrix([[2, 4, 6, 4], [2, 5, 7, 6], [2, 3, 5, 2]])
A = Matrix([[2, 8, 7], [9, 7, 4]])
# b = Matrix([1,3,1])
# b = Matrix([4,3,5])
b = Matrix([5, 8])
xp, xs, fc = completeSol(A, b)
print("xp = \n")
print(xp)

print("xs = \n")
print(xs)

print("free columns are: ", fc)

input("\nPress Enter to continue.")