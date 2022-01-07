import numpy as np;

def matrandom(num):
    return np.random.randint(low = 1, high = 9, size = (num,num))

def matelim_sub(matrix, pivot):
    elim = np.eye(len(matrix))

    for i in range(pivot + 1, len(matrix)):
        if(matrix[pivot, pivot] == 0):
            matrix[[pivot, pivot + 1]] = matrix[[pivot + 1, pivot]]
        elim[i, pivot] = -matrix[i, pivot]/ matrix[pivot, pivot]

    return elim

def matelim(matrix):
    if (not len(matrix) or len(matrix) != len(matrix[0])):
        print("error: the matrix is not 3x3")
        return

    print("\nA = \n", matrix)
    newE = np.eye(len(matrix))

    for i in range(len(matrix) - 1):
        E = matelim_sub(matrix, i)
        newE = newE @ E
        EA = E @ matrix
        matrix = EA
        print("\nE at each Position = \n", np.around(E, 3), "_____", i)  # seeing by followed through this -> E21, E31, E32

    print("\nE (already multiply all E) = \n", np.around(newE, 3))
    print("\nEA = \n", np.around(matrix, 3))


# C = np.random.randint(low=1, high=9, size=(3,2))
# matelim(C)

A = np.array([[4,4,5], [3,7,3], [4,5,7]])
# A = np.array([[2,1,0], [1,2,1], [0,1,2]])
# A = np.array([[1,2,1], [3,8,1], [0,4,1]])
# A = matrandom(3)
matelim(A)
