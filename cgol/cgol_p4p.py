"""Conway's Game of Life

The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970. It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves. It is Turing complete and can simulate a universal constructor or any other Turing machine.

The universe of the Game of Life is [a ...], two-dimensional orthogonal grid of [...] cells, each of which is in one of two possible states, live or dead [...]. Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:

- Any live cell with fewer than two live neighbours dies, as if by underpopulation.
- Any live cell with two or three live neighbours lives on to the next generation.
- Any live cell with more than three live neighbours dies, as if by overpopulation.
- Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

[...]
The initial pattern constitutes the seed of the system. The first generation is created by applying the above rules simultaneously to every cell in the seed; births and deaths occur simultaneously, and the discrete moment at which this happens is sometimes called a tick. Each generation is a pure function of the preceding one. The rules continue to be applied repeatedly to create further generations.

- Wikipedia on Conway's game of life [adapted for p4p]
"""

# Programm does not catch anything but a keyboard interupt to save the game

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
    """update the world <cycles> number of times

    Args:

        world (np.array):  the world to be updated
        cycles (int):      the number of cycles to go through

    Returns:
        new_world (np.array): the state of the world after <cycles> updates.
    """
    start_time = time.time()
    interval = 1/cycles
    #120 cycles at intended 2Hz, max runtime of 1Minute
    for i in range(1,121):
        try:
            time.sleep(start_time + i*interval - time.time())
            world = update(world)
            print(world)
            i=i+1
        except KeyboardInterrupt:
            #Save after interrupt
            print("\nProgramm interupted by user.")
            print(world)
            escape(world)
    return world


def load(filename):
    """Load a saved pattern (Hint: Pay attention to the delimiter that separates values. Here, we want to use a comma (,))

    Args:
        filename (str): the path to a saved game (csv)

    Returns:
        (np.array): a CGoL world
    """
    print("Opening file\n" + filename)
    file = open(filename)
    world = loadtxt(file, delimiter = ",")
    return world


def save(filename, world):
    """Save world to filename as csv.

    Args:
        filename (str): the path to save the world to.
        world (np.array): the world to save
    """
    np.savetxt(filename, world, delimiter=",")


def escape(world):
    print("Input seed to save current game state under.")
    filename = (r"C:\Users\sabse\Documents\Python\cgol\seeds\seed_" + input("seed_") + ".csv")
    #Programm doesn't save when no seed is given
    if not filename == r"C:\Users\sabse\Documents\Python\cgol\seeds\seed_.csv":
        save(filename, world)
    print("Programm is exiting.")
    #The End
    exit()


def main():
    """
    A random world is initialised by passing a shape or an existing world is loaded by passing a filename,
    and runs at 2 iterations per second until a KeyboardInterrupt is risen.
    It then queries a filename to save to and leaves.
    """
    #Choose mode
    print("Conway's game of life\nChoose a mode:\n(1) Random game \n(2) Load file")
    mode = int(input())
    #Load from seed
    if (mode - 1):
        print("Input seed you wish to load:")
        filename = (r"C:\Users\sabse\Documents\Python\cgol\seeds\seed_" + input("seed_") + ".csv")
        world = load(filename)
    #Generate random world
    elif not (mode - 1):
        x = int(input("Set shape of the world: \nx="))
        y = int(input("y="))
        shape = (y,x)
        world = init_world(shape)
    print(world)

    #Run it
    _run(world)
    


if __name__ == "__main__":
    main()