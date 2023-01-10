import numpy as np
from numpy import loadtxt
file = open('~/p4p/ex2/cgol/data/glider.csv', 'rb')
arr = loadtxt(file,delimiter = ",")
arr = arr.transpose()
np.savetxt("my_arr.csv", arr, delimiter=",")