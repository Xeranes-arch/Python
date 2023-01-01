"""Bullseye

Write a proper docstring here such that:
    - if the flag `--seed SEED` is provided, the seed SEED should be used to generate random numbers
    - if the flag `--games GAMES` is provided, the program should run GAMES number of games

Have a look at https://docopt.org on how to do this

Usage: 

Options:
  --seed     Give seed
  --games    Number of Games to be played [default: 10]
"""

import math
import random
import docopt

__version__ = "0.2.0"

def get_opts():
    """get the options passed to the program via docopt

        Returns:
            options (dict): a dictionary with the options
    """
    options = docopt.docopt(__doc__)
    return options


def update(x, y, r):
    """Update the radius according to the rules of the game.

    If the hit is on the disk, i.e. :math:`x_i**2+y_i**2 <= r_i**2`, the new radius
    :math:`r_{i+1}` will be the length of the side opposing
    :math:`\sphericalangle O-\left(x,y\right)-B` in the right triangle :math:`\Delta
    O-\left(x,y\right)-B`, where :math:`O` is the origin of the circle,
    :math:`\left(x, y\right)` the position the dart hit and :math:`B` the point
    intersecting the circle and the line perpendicular to
    :math:`\vec{O\left(x,y\right)}`.
    
    If the hit is not on the disk, return the number -1, indicating a clear miss (as the new radius cannot be smaller than zero).
    This way, you will later know when the board was missed.

    Args:
      x (float): x coordinate of the dart
      y (float): y coordinate of the dart
      r (float): the radius of the dart board

    Returns:
        (float): the new radius if the disk was hit, -1 otherwise
    """
    r_hit_sq = x**2 + y**2
    r_cur_sq = r**2
    if r_hit_sq <= r_cur_sq:
      #hit
      r_new = math.sqrt(r_cur_sq - r_hit_sq)
    else:
      #miss
      r_new = -1
    return r_new


def game():
    """One game of hitting the dart board until we miss

    First, we set the radius to 1, as this is the radius of the disk we want to start with.
    We also initialize a new variable to keep track of the score, i.e. the number of darts thrown until
    the board was missed (including the dart that missed). So, for example, if the first dart already misses the disk,
    the score should still be 1.

    Then, until we missed, we throw to a random point (x, y), update the radius using the update function above and increase the score by one.
    When a dart misses the board, the game ends and the final score is returned.

    Returns:
      score (int): the number of darts thrown.
    """
    r = 1
    i = 0
    while r!=-1:
      x = random.uniform(-1,1)
      y = random.uniform(-1,1)
      r = update(x,y,r)
      i = i+1
    return i 


def main(opts, games=10):
    """for a given number of games, record the scores, then return the mean and
    of the scores
    If the options contain a seed for the random number generartor, pass this seed to numpy
    If the options contain a number of games to be played, play the game this many times

    Args:
      games (int): the number of games to play.

    Returns:
      mean (float):  the mean value of the scores
    """
    print(opts)
    if opts['<SEED>'] != None:
      random.seed(opts['<SEED>'])
    if opts['<GAMES>'] != None:
      games = opts['<GAMES>']
    
    scores = [0]*games
    dev = [0]*games
    for i in range(games):
      scores[i] = game()
      dev[i] = (math.pi/4) - scores[i]
      i = i + 1
    mean = sum(scores)/games
    sdv = math.sqrt(abs(sum(dev))/games)
    print(sdv)
    return mean


if __name__ == "__main__":
    """This code executes when the program is run from the command line"""
    opts = get_opts()
    mean = main(opts, 100000)
    print(f"exp(pi/4) approx equal to {mean}")
