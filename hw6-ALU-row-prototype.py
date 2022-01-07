import numpy as np

def elimination_matrix(A, row):
    I = np.eye(3)



def find_U(A):
    L = np.eye(3)
    temp_row = 0
    for i in range(3):
        zeroPos = [A[1, 0], A[2, 0], A[2, 1]]
        minusUse = [A[0, 0], A[0, 0], A[1, 1]]

        if(zeroPos[i] != 0):
            factor = zeroPos[i] / minusUse[i]
            if i == 0:
                temp_row = A[0,:] * factor
                A[1,:] = A[1,:] - temp_row  # เอามา row ลบกัน โดยใช้ row ของ arr เปนตัวตั้ง
                L[2, 0] = factor
            elif i == 1:
                temp_row = A[0,:] * factor
                A[2,:] = A[2,:] - temp_row
                L[2, 1] = factor
            elif i == 2:
                temp_row = A[1,:] * factor
                A[2,:] = A[2,:] - temp_row
                L[2, 2] = factor
        L[2, 0] = factor
    # return np.around(A, 3)
    U = np.around(A, 3)

    return L, U


# main program
# A = np.array([[1,2,1], [3,8,1], [0,4,1]], dtype = float)
# A = np.array([[2,1,0], [1,2,1], [0,1,2]], dtype = float)
A = np.array([[1,2,1], [0,1,1], [2,7,9]], dtype = int)

(L, U) = find_U(A)
print("L: \n", L)
print("U: \n", U)
