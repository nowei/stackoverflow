import numpy as np
B1=np.array([[1,2],[3,4]])

A=np.zeros((2,2,2))

A[:] = B1
print(A)