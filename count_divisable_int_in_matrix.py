import numpy as np
import random

rand_arr = np.random.randint(10, size=(random.randint(1,10),random.randint(1,10)))

def count_div_by_5(matrix):
    arr = matrix
    len_arr = arr.shape[0]*arr.shape[1]
    arr = arr.reshape((1,len_arr))
    count = 0
    for i in range(len_arr):
        if (arr[0,i]%5 == 0) and (arr[0,i]!=0):    
            print(arr[0,i])
            count = count + 1   
    return count

print(rand_arr)
print(count_div_by_5(rand_arr))
print((rand_arr.shape[0]*rand_arr.shape[1]))