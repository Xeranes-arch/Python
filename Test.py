import numpy as np
from numpy import loadtxt

shape = (5,4)
world = np.random.randint(0,2,shape)


print(world)

print("Give Filename:")
seed = input("seed_")
np.savetxt((seed), world)

file = open(seed)
world = loadtxt(file)

print(world)