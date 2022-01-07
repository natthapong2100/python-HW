import numpy as np


E21 = np.array([[1,0,0], [-0.5,1,0], [0,0,1]])
E32 = np.array([[1,0,0], [0,1,0], [0,-2/3,1]])
A = np.array([[2,1,0], [1,2,1], [0,1,2]])
I = np.eye(3)  # จะให้ E31 เปน identity ก็ได้ แต่คูณไปก็จะไม่มีผล ex. A @ invA = I -> A = AI
print("I = \n", I)

# calculate U
U = E32 @ E21 @ A
print("U = \n", U)

# calculate L
# E21[1,0] = 1/2  # make it to inverse
# print("\new E21: \n", E21)
# E32[2,1] = 2/3
# print("new E32: \n", E32)

invE21 = np.linalg.inv(E21)
invE32 = np.linalg.inv(E32)
print("Inverse: \n", invE21)
print(invE32)
print()

L = invE21 @ invE32
print("\nL = \n", L)

# prove A = LU
A_check = L @ U
print("prove A = LU, A = \n", A_check)  # correct prove, need to beware about must write the correct variable

