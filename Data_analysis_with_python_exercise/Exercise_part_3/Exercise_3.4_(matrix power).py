import numpy as np
from functools import reduce
def matrix_power(a, n):
    if a.shape[0]!=a.shape[1]:
        return "Matrix is not square"
    if n==0:
        return np.eye(a.shape[0])
    elif n>0:
        return reduce(np.matmul,(a for _ in range (n)))
    else:
        inv_a= np.linalg.inv(a)
        return reduce(np.matmul,(inv_a for _ in range (-n)))

np.random.seed(0)
a = np.random.randint(0, 10, (3, 3))
print(a)
print(matrix_power(a, 4))
print(matrix_power(a, -4))
print(matrix_power(a, 0))