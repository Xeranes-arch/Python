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
        self.last_move = None

    def __str__(self):
        """A nice printable representation of the board

            Returns:
                String containing the printable representation of the board
        """
        out = "\n  " + self.grid[0, 0] + "  |  " + self.grid[0, 1] + \
            "  |  " + self.grid[0, 2] + "\n-----|-----|-----\n" + \
            "  " + self.grid[1, 0] + "  |  " + self.grid[1, 1] + \
            "  |  " + self.grid[1, 2] + "\n-----|-----|-----\n" + \
            "  " + self.grid[2, 0] + "  |  " + \
            self.grid[2, 1] + "  |  " + self.grid[2, 2] + "\n"
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
        self.grid[position_to_coordinates(position)] = marker
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
        # arr_bool of X's=1 O's=-1 and ""=0
        arr_bool = np.zeros_like(self.grid, dtype=int) \
            + arr_X - arr_O
        # sum up the cols and rows
        arr_col = arr_bool[0, :] + arr_bool[1, :] + arr_bool[2, :]
        arr_row = arr_bool[:, 0] + arr_bool[:, 1] + arr_bool[:, 2]
        dia = adi = 0
        # if any 3 or -3 there's a win
        for i in range(3):
            dia += arr_bool[i, i]
            adi += np.flip(arr_bool, axis=0)[i, i]
        if 3 in (*arr_col, *arr_row, dia, adi):
            raise TimeoutError("X wins")
        if -3 in (*arr_col, *arr_row, dia, adi):
            raise TimeoutError("O wins")

    def is_full(self):
        """Checks if the grid is full and, if so, raises an IndexError"""
        n = 0
        for i in range(self.grid.size):
            # count up when grid isn't empty
            bo = False
            if self.grid[position_to_coordinates(i+1)] != "":
                n += 1
            if n == 9:
                print(self)
                print("Game has been drawn.")
                raise EOFError("Game is drawn.")


def position_to_coordinates(position):
    """helper function: converts a given position (1 - 9) to coordinates (row, col) on the grid"""
    col = position % 3 - 1
    n = 1
    while position > 3:
        position = position - 3
        n = n + 1
    row = n - 1
    return ((row, col))


class Player():
    """A player for the game

    Args:
        name (str):  the player's name
        marker (str): a marker for the player. Either X or O
    """

    def __init__(self, name, marker):
        self.name = name
        self.marker = marker

    def __str__(self):
        """The representation of Player is their name, so this method should return it"""
        return self.name

    @property
    def name(self):
        """Getter for the name variable

        Returns:
            Player's name
        """
        return self.__name

    @name.setter
    def name(self, value):
        """Setter for the name variable. It should prevent setting the name to an empty string by raising a ValueError

        Args:
            value (str): The string that should be set as the player's name

        """
        if value == "":
            raise ValueError("Empty name is not permitted.")
        else:
            self.__name = value

    @property
    def marker(self):
        """Getter for the marker variable

        Returns:
            Player's marker
        """
        return self.__marker

    @marker.setter
    def marker(self, value):
        """Setter fo the marker variable. It should prevent setting the marker to anything other than X or O (case insensitive) and transform every given value into upper case.
        When passed an illegal value, it should raise a ValueError

        Args:
            value (str): The marker that should be set for the player (either X or O, case insensitive)
        """
        if value.upper() == "X" or value.upper() == "O":
            self.__marker = value.upper()
        else:
            raise ValueError("only X or O are valid players")


class Game():
    """A game of tictactoe"""

    def __init__(self, name_1="Alice", name_2="Bob", statistics="stats.json"):
        """Initialises a Game of TicTacToe

        Args:
          name_1 (str): the name of Player 1
          name_2 (str): the name of Player 2
          statistics (str): hall of fame filename to write the winner to

        Attr:
          self.board (Board): a board object
          self.player_1 (Player): will evaluate to Player with marker X
          self.player_2 (Player): will evaluate to Player with marker O
          self.statistics (str): hall of fame filename to write the winner to
          self._current (Player): The player that is to move next. Should be initialized by setting it to player_1
        """
        self.board = Board()
        self.player_1 = name_1
        self.player_2 = name_2
        self.statistics = statistics
        self.current = self.player_1

    @property
    def player_1(self):
        """Player 1"""
        return self.__player_1

    @player_1.setter
    def player_1(self, value):
        """Set player 1"""
        self.__player_1 = Player(value, "X")

    @property
    def player_2(self):
        """Player 2"""
        return self.__player_2

    @player_2.setter
    def player_2(self, value):
        """Set player 2"""
        self.__player_2 = Player(value, "O")

    def make_move(self):
        """Let the player in self._current make one move

         - get the current player's desired spot by running the ``query_spot`` method
         - put the player's marker down in the selected spot returned by the ``query_spot`` method. 
           Don't forget to handle errors raised by invalid moves and run the ``query_spot`` method again if
           necessary until a valid choice was made. 
         - check if a win has occurred: if so, raise a TimeoutError with a cheerful message and write to stats file using write_stats
         - check if a draw has occurred: if so, raise a EOFError with a draw message
         - Set self._current to other player
         """
        # Rerun query spot until input is valid
        while True:
            try:
                spot = self.query_spot()
                Board.place(self.board, spot, self.current.marker)
                break
            except ValueError:
                print("Invalid spot, please choose again.")
                pass
        # Catch win and call write_stats
        try:
            Board.has_won(self.board)
        except TimeoutError:
            self.write_stats(self.current.name, self.statistics)
            print(self.board)
            print("Congratulations " + self.current.name +"! You've won.")
            raise TimeoutError(self.current.name + " has won!")
        # Catch draw
        Board.is_full(self.board)
        # Change Player
        if self.current == self.player_1:
            self.current = self.player_2
        else:
            self.current = self.player_1

    def query_spot(self):
        """
        Ask the player for a spot, then determine if the answer is an integer.
        If not, check if it was a "Q" or "q".
        If so, end the game without result by raising an EOFError.

        Return:
            The spot (int) the player chose for their marker

        """
        spot = input("Choose spot to place your marker, " + self.current.name + ":")
        # Catch quit
        if spot.upper() == "Q":
            raise EOFError("Quit.")
        # Catch non int
        if type(int(spot)) != int:
            raise ValueError("Not an Integer.")
        return int(spot)

    def write_stats(self, player, filename):
        """appends the winner with timestamp to the statistics

        Args:
          player (str):   name to write down
          filename (str): filename of the hall of fame (assume it is a json)
        """
        #file = open(self.statistics)
        file = open(
            "C:\\Users\\Xeonis7\\Documents\\Python\\ex4\\tictactoe\\src\\stats.json")
        halloffame = json.load(file)
        new_winner = "Winner " + str(int(((list(halloffame.keys())[-1]).split(" "))[-1]) + 1)
        halloffame[new_winner] = self.current.name
        with open("C:\\Users\\Xeonis7\\Documents\\Python\\ex4\\tictactoe\\src\\stats.json", 'w') as f:
            json.dump(halloffame, f)
