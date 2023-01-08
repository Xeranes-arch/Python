"""A game of TicTacToe"""


import json
import pickle

import numpy as np

from datetime import datetime
from warnings import warn

__version__ = "0.1.0"

class Board():
    """A grid of 3 by 3 where players can place
    their markers."""


    def __init__(self):
        """A Board for the game TicTacToe

        Attr:
          grid (np.array):   a grid onto which players can put their markers.
          last_move (int): the position of the last played marker.
        """
        pass


    def __str__(self):
        """A nice printable representation of the board

            Returns:
                String containing the printable representation of the board
        """
        pass


    def place(self, position, marker="X"):
        """Place a marker in the given spot

        First checks if the spot chosen is valid. If the index does not
        exist (not between 1 and 9), raise a ValueError, saying the spot is out of bounds. If the
        spot is already taken, raise a ValueError saying that the spot is taken.

            TODO: maybe it would be best to put this check in a helper function
            ``is_valid(position)``

        Then, we place the marker in the given location on the grid.

        We record the position in self.last_move

        Args:
          self:  it is class method
          position (int): the position (between 1 and 9) where the marker should be placed. The positions on the grid must be as follows:

          1 | 2 | 3
          ---------
          4 | 5 | 6
          ---------
          7 | 8 | 9

          marker (str): X or O, the marker of the player
        """
        pass


    def is_valid(self, position):
        """helper function to determine if the move is allowed

        If the index does not exist, raise a ValueError, saying the position is
        out of bounds. If the position is taken, raise a ValueError saying that
        the spot is already taken.

        Args:
          position (int): the position number to be checked for validity

        Returns:
          Nothing. It either succeeds or raises an error.

        TODO: reconcile with Game.make_move
        """
        pass


    def show_marker(self, marker):
        """
        Returns an array of booleans where all spots with markers of either X or O (specified in the method's arguments) 

        Example:
            Board is:
            
            [["X", "X", "O"],
             ["X", "O", "X"],
             ["X", "",  ""]]
            
            show_marker("X") returns:

            [[True, True, False],
             [True, False, True],
             [True, False, False]]

        Args:
          - marker (str):  the chosen marker whose position will be True in the returned array

        Returns:
          - (np.array): An array with <marker> as ``True``, the rest ``False``.

        """
        pass


    def has_won(self):
        """check if one of the four winning conditions has occurred:

        - "horizontal"
        - "vertical"
        - "falling_diag"
        - "rising_diag"

        and rise a TimeoutError with the player's marker as the text if the game is won.
        """
        pass


    def is_full(self):
        """Checks if the grid is full and, if so, raises an IndexError"""
        pass

def position_to_coordinates(position):
    """helper function: converts a given position (1 - 9) to coordinates (row, col) on the grid"""
    pass

def diagonal(grid):
    """helper function: find the diagonal of the board"""
    pass


def antidiagonal(grid):
    """helper function: find the antidiagonal of the board"""
    pass
