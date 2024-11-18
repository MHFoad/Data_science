import numpy as np
def column_comprassion(a_2d):
    second_column=a_2d[:,1]
    second_last_coulmn=a_2d[:, -2]
    condition= second_column>second_last_coulmn
    print(condition)
    return a_2d[condition]
arr=np.random.randint(0,20, (5,4))
print(arr,"\n")
print(column_comprassion(arr))