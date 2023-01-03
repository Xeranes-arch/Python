"""Bullseye

Write a proper docstring here such that:
    - if the flag `--seed SEED` is provided, the seed SEED should be used to generate random numbers
    - if the flag `--games GAMES` is provided, the program should run GAMES number of games

Have a look at https://docopt.org on how to do this

Usage:
    bullseye.py
    bullseye.py --seed=SEED
    bullseye.py --games=GAMES
    bullseye.py --seed=SEED --games=GAMES
"""

import numpy as np
import docopt

__version__ = "0.2.0"


def get_opts():
    """get the options passed to the program via docopt

        Returns:
            options (dict): a dictionary with the options
    """
    return docopt.docopt(__doc__)


def update(x, y, r):
    """Update the radius according to the rules of the game.

    If the hit is on the disk, i.e. :math:`x_i**2+y_i**2 <= r_i**2`, the new radius
    :math:`r_{i+1}` will be the length of the side opposing
    :math:`\sphericalangle O-\left(x,y\right)-B` in the right triangle :math:`\Delta
    O-\left(x,y\right)-B`, where :math:`O` is the origin of the circle,
    :math:`\left(x, y\right)` the position the dart hit and :math:`B` the point
    intersecting the circle and the line perpendicular to
    :math:`\vec{O\left(x,y\right)}`.

    Args:
      x (float): x coordinate of the dart
      y (float): y coordinate of the dart
      r (float): the radius of the dart board

    Returns:
        (float): the new radius
    """
    # Distance from centre to where the dart landed squared
    centre_distance_squared = x**2 + y**2
    # This would solve the Test, but makes no sense in the program whatsoever
    if centre_distance_squared > r**2:
        raise AssertionError
    return np.sqrt(r**2 - centre_distance_squared)


def game():
    """One game of hitting the dart board until we miss

    First, we set the radius to 1 and the score to 0.
    Then, as long as we hit the board, add 1 to the scores for each dart thrown, throw to a random
    (x,y) coordinate, update the new radius or end the game if we missed.
    Finally return the number of scores.

    Returns:
      score (int): the number of darts thrown.
    """
    r = 1
    score = 1
    while True:
        # gives x and y a random number between 0 and 1
        x, y = np.random.uniform(-1, 1, 2)
        # check whether the dart would hit
        if x**2 + y**2 >= r**2:
            return score
        r = update(x, y, r)
        score += 1


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
    if opts is not None:
        if opts["--games"] is not None:
            games = int(opts["--games"])
        if opts["--seed"] is not None:
            np.random.seed(int(opts["--seed"]))
    sum_of_scores = 0
    for i in range(games):
        sum_of_scores += game()
    return sum_of_scores/games


if __name__ == "__main__":
    """This code executes when the program is run from the command line"""
    opts = get_opts()
    mean = main(opts, 100000)
    print(f"exp(pi/4) approx equal to {mean}")
