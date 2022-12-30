import numpy as np
from numpy import loadtxt


shape = (5,4)
world = np.random.randint(0,2,shape)
print(world)

world_p = world
world_p = world_p.astype(str)
world_p = np.char.replace(world_p,'1',(u'\u2588\u2588'))
world_p = np.char.replace(world_p,'0',(u'\u0020\u0020'))
world_p = np.array2string(world_p, separator='', formatter={'str_kind': lambda world_p: world_p})
print(world_p)