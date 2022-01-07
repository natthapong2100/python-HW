import numpy as np

x = np.array([[1,0,0], [1,1,0], [1,1,1]])

ans = np.linalg.inv(x)

print("Ans: ", ans)