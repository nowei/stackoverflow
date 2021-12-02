import numpy as np
data1 = []
A = np.random.normal(0, 1, (20, 5))
m1 = np.random.normal(0, 1, (5))  # center of clusters
print(np.matmul(A,m1).shape)
print(np.random.normal(np.matmul(A,m1)).shape)
for _ in range(1):
    data1.append(np.random.normal(np.matmul(A, m1), np.identity(20)))
print(np.matmul(A, m1))
print(data1[0].shape)
x1 = np.vstack(data1) # x1.shape -> (1000, 20)
print(x1) 
print(np.matmul(A, m1))
# print(np.average(x1, axis=0))
print(x1.shape)