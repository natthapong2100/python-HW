import numpy as np

# A = np.array([[2,1,0], [1,2,1], [0,1,2]])
# # A[0,:] = A[0,:] * 2  # multiply row "can search numpy array ค้นรูป"
# x = 9
# A[0,:] = [x, 5, 5]
# print("Ans: \n", A)
# print("show column: \n", A[:,2])
# print("ok: ", A[2, 1])

A = np.array([[6,-7], [-6,3]])
print("A: \n", A)
print("inverse of A: \n", np.linalg.inv(A))

print()
temp = np.eye(2)
temp[0,:] = A[0,:]
A[0,:] = A[1,:]
A[1,:] = temp[0,:]
print("Ans: \n", A)