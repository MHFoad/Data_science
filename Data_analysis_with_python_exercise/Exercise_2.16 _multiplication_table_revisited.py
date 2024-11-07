import numpy as np
def multiplication_table(n):
    arr=np.arange(n)
    arr1=arr.reshape(n,-1)
    result=arr*arr1
    return result
print(multiplication_table(4))