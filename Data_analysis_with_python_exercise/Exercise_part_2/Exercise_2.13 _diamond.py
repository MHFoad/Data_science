import numpy as np
def daimond(n):
    a=np.eye(n, dtype=int)
    b=a[1:n,::-1]
    c=np.concatenate((a,b))
    d=c[:, 1:][:, ::-1]
    e=np.concatenate((d,c), axis=1)
    return e

print(daimond(3))