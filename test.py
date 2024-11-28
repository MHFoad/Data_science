import numpy as np
s=np.array([[1, 6, 7],
 [7, 8, 1],
 [5, 9, 8]])

x=np.array([1,4,2])
print(x.shape)
y = np.matmul(s,x)
print("y=", y, sep="\n")