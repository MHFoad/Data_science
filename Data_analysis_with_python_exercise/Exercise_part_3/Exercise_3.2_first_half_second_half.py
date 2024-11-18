import numpy as np
def first_half_second_half(a):
    m=a.shape[1]//2
    matrix=np.sum(a[:, :m], axis=1)> np.sum(a[:, m:], axis=1)
    return a[matrix]

a = np.array([[1, 3, 4, 2],
              [2, 2, 1, 2]])
print(first_half_second_half(a))