import numpy as np
def vector_lengths(vector_2d):
    length=np.sqrt(np.sum(vector_2d**2,axis=1))
    return length
np.random.seed(0)
a=np.random.randint(0,10,(4,5))
print(a)
print(vector_lengths(a))