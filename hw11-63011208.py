import numpy as np

def projection(A, b):
    AT = A.T
    ATA = AT @ A
    ATb = (AT @ b)
    x = np.linalg.inv(ATA) @ ATb
    p = A @ x
    e = b - p
    P = A @ np.linalg.inv(ATA) @ AT
    values_of_a = []
    for i in range(len(AT)):
        values_of_a.append(A[:, i:i + 1])
    for j in range(len(values_of_a)):
        result = e.T @ values_of_a[j]
        trueornot = np.all((result == 0))
        if (trueornot == False):
            return "X is invalid.", "p is invalid", "P is invalid"

    return x, p, P


A = np.array([[1, 0], [1, 1], [1, 2]])
b = np.array([[6, 0, 0]]).T
print("\nA=\n", A)
print("\nb=\n", b)
[x, p, P] = projection(A, b)
print("\nx=\n", x)
print("\np=\n", p)
print("\nP=\n", P)
