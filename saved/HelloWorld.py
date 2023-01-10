import numpy as np
import random

rand_arr = np.random.randint(10, size=(random.randint(1,10),random.randint(1,10)))

def shift_matrix_east(arr):
    for i in range(arr.shape[1]-1,0,-1):
        arr[:,i] = arr[:,i-1]
            
    arr[:,0] = 0
    return arr
    
print(shift_matrix_east(rand_arr))