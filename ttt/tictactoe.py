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
        self.grid = np.empty(shape=(3, 3), dtype=str)
        self.grid = np.where(self.grid == "", "O", "X")
        self.last_move = None

    def __str__(self):
        """A nice printable representation of the board

            Returns:
                String containing the printable representation of the board
        """
        out = "\n  " + self.grid[0, 0] + "  |  " + self.grid[0, 1] + \
            "  |  " + self.grid[0, 2] + "\n-----|-----|-----\n" + \
            "  " + self.grid[0, 0] + "  |  " + self.grid[0, 1] + \
            "  |  " + self.grid[0, 2] + "\n-----|-----|-----\n" + \
            "  " + self.grid[0, 0] + "  |  " + \
            self.grid[0, 1] + "  |  " + self.grid[0, 1] + "\n"
        return out

    def place(self, position, marker="X"):
        """Place a marker in the given spot

        First checks if the spot chosen is valid. If the index does not
        exist (not between 1 and 9), raise a ValueError, saying the spot is out of bounds. If the
        spot is already taken, raise a ValueError saying that the spot is taken.

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
        self.is_valid(position)
        self[position_to_coordinates(position)] = marker
        self.last_move = position

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
        print(position)
        if position < 1 or position > 9:
            raise ValueError("the position is out of bounds")
        if self.grid[position_to_coordinates(position)] != "":
            raise ValueError("the spot is already taken")

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
        # haha oneliner
        return np.where(self.grid == marker, True, False)

    def has_won(self):
        """check if one of the four winning conditions has occurred:

        - "horizontal"
        - "vertical"
        - "falling_diag"
        - "rising_diag"

        and rise a TimeoutError with the player's marker as the text if the game is won.
        """
        arr_X = self.show_marker("X").astype(int)
        arr_O = self.show_marker("O").astype(int)
        # arr_bool of X=1 O=-1 and ""=0
        arr_bool = np.zeros_like(self.grid, dtype=int) \
            + arr_X - arr_O
        # sum up the cols and rows
        arr_col = arr_row = np.copy(arr_bool)
        arr_col[0, :] = arr_bool[0, :] + arr_bool[1, :] + arr_bool[2, :]
        arr_row[:, 0] = arr_bool[:, 0] + arr_bool[:, 1] + arr_bool[:, 2]
        dia = adi = 0
        # if any 3 or -3 there's a win
        for i in range(3):
            dia += arr_bool[i, i]
            adi += np.flip(arr_bool, axis=0)[i, i]
        if 3 in (*arr_col[0, :], *arr_row[:, 0], dia, adi):
            raise TimeoutError("X wins")
        if -3 in (*arr_col[0, :], *arr_row[:, 0], dia, adi):
            raise TimeoutError("O wins")

    def is_full(self):
        """Checks if the grid is full and, if so, raises an IndexError"""
        n = 0
        for i in range(self.grid.size):
            # count up when grid isn't empty
            if self.grid[position_to_coordinates(i+1)] != "":
                n += 1
            if n == 9:
                raise TimeoutError("Board is full.")


def position_to_coordinates(position):
    """helper function: converts a given position (1 - 9) to coordinates (row, col) on the grid"""
    col = position % 3 - 1
    n = 1
    while position > 3:
        position = position - 3
        n = n + 1
    row = n - 1
    return ((row, col))


board = Board()
print(board.__str__())
