import time
import numpy as np
from numpy import loadtxt

def init_world(shape):
    world = np.zeros(shape, dtype=bool)
    return world


def neighbours(world):
    count = 0
    alive_neighbours = np.zeros((world.shape[0],world.shape[1]),dtype=int)
    #loop over all indizes x,y of world
    for y in range(world.shape[0]):
        for x in range(world.shape[1]):
            #bounds of 3x3 grid around current cell
            x_0 = x - 1
            x_1 = x + 1
            y_0 = y - 1
            y_1 = y + 1
            #loop over grid, count live neighbours
            for j in range(y_0, y_1+1):
                for i in range(x_0, x_1+1):
                    #making sure world borders aren't crossed
                    if i < 0 or i > world.shape[1]-1 or j < 0 or j > world.shape[0]-1:
                        continue
                    count = count + world[j,i]
            #write alive_neighbours, "- world[y,x]" to subtract cells own value from 3x3 grid
            alive_neighbours[y,x] = count - world[y,x]
            count = 0
    return alive_neighbours


def update(world):
    new_world = neighbours(world)
    for y in range(world.shape[0]):
        for x in range(world.shape[1]):
            #updating live cells
            if world[y,x] == 1 and (new_world[y,x] < 2 or new_world[y,x] > 3):
                new_world[y,x] = 0
            #updating dead cells
            elif world[y,x] == 0 and new_world[y,x] == 3:
                new_world[y,x] = 1
            #rest stays the same
            else:
                new_world[y,x] = world[y,x] 
    return new_world


def _run(world, cycles=2):
    #120 cycles at intended 2Hz, max runtime of 1Minute
    for i in range(cycles):
        world = update(world)
        i=i+1        
    return world


def load(filename):
    file = open(filename)
    world = loadtxt(file, delimiter = ",")
    return world


def save(filename, world):
    np.savetxt(filename, world, delimiter=",")


def main():
    #Choose mode
    print("Conway's game of life\nChoose a mode:\n(1) Random game \n(2) Load file")
    mode = int(input())
    #Load from seed
    if (mode - 1):
        print("Input seed you wish to load:")
        filename = input()
        world = load(filename)
    #Generate random world
    elif not (mode - 1):
        shape = input("Shape:")
        world = init_world(shape)
    #Run it
    start_time = time.time()
    for i in range(1,11):
        try:
            time.sleep(start_time + i - time.time())
            _run(world)
            print(world)
        except KeyboardInterrupt:
            #Save after interrupt
            print("\nProgramm interupted by user.")
            filename = input()
            save(filename, world)
            exit()
        i = i + 1


if __name__ == "__main__":
    main()