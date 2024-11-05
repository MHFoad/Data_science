import numpy as np
def get_rows(d_arrays):
    return [d_arrays[n] for n in range (d_arrays.shape[0])]
def get_columns(d_arrays):
    d_arrays=d_arrays.T
    return [d_arrays[n] for n in range(d_arrays.shape[0])]

a = np.array([[5, 0, 3, 3],
 [7, 9, 3, 5],
 [2, 4, 7, 6],
 [8, 8, 1, 6]])
print(get_rows(a))
print()
print(get_columns(a))