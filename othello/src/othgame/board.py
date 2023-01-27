import numpy as np

class Board():
    """
    Board implements a class for the 8x8 board of the game Othello.
    Player discs are represented with integers 1 and 2, empty slots with 0.
    Coordinates are a combination of a capital letter and a number (e.g, A1, D3, ...)
    """


    def __init__(self):
        """Constructor for the class Board"""
        
        self._b = np.zeros((8,8), dtype = int)     # empty board
        self._b[3:5,3:5] = np.array([[1,2],[2,1]]) # starting pieces


    def marker(self, player):
        """
        Returns the marker for player (integer: 1 or 2)
        Raises ValueError if player is not known
        """

        if not player in [1, 2]:
            raise ValueError(f"Error: {player} not known")

        return "@O"[player-1]


    def ndiscs(self, player):
        """Returns the number of discs for player (integer: 1 or 2)
        Raises ValueError if player is not known"""

        if not player in [1, 2]:
            raise ValueError(f"Error: {player} not known")

        return np.sum(self._b == player)


    def _is_on_board(self, coord):
        """Returns True if coord is on board, False otherwise"""

        if any(coord >= np.array((8,8))) or any(coord < np.array((0,0))):
            return False
        else:
            return True


    def _str2coord(self, pos):
        """
        Returns the coordinate corresponding to the string
        Raises ValueError if not possible
        """
        lett = "ABCDEFGH"
        numb = "12345678"
        
        # convert the position to actual coordinates
        c = np.array([lett.index(pos[0]), numb.index(pos[1])])
        if not self._is_on_board(c):
            raise ValueError

        return c


    def place(self, pos, player, flank = True):
        """
        Places a new disc from player at position pos (string, f.ex. 'A1').
        Raises ValueError if player (integer: 1 or 2) is not known, position is not free or move is illegal
        If flank is True, flanks the enclosed discs 
        Returns the number of discs to flank
        """

        players = [1, 2]

        if not player in players:
            raise ValueError(f"Error: {player} not known")

        try:
            c = self._str2coord(pos)
        except:
            raise ValueError(f"Error: {pos} is not a valid coordinate")

        # check that the coordinate is not occupied
        if self._b[tuple(c)] != 0:
            raise ValueError(f"Error: {pos} is not free")
        
        # all directions to check for enclosed discs
        directions = ((1,1), (1,-1), (-1,-1), (-1,1),\
                      (1,0), (-1,0),\
                      (0,1), (0,-1))
        
        # find all discs to flank in all directions
        toflank = []
        for d in directions:
            coords = []
            nextc = np.array(c)
            while True:
                nextc += d
                if not self._is_on_board(nextc) or self._b[tuple(nextc)] == 0:
                    coords = []
                    break
                if self._b[tuple(nextc)] == player:
                    break
                else:
                    coords.append(tuple(nextc))
            toflank += coords
        
        if len(toflank) == 0:
            
            # only moves that lead flanking are legal
            raise ValueError(f"Error: {pos} is an illegal move")

        else:

            # flank all discs, if this is wanted
            if flank:
                for cf in toflank:
                    self._b[tuple(cf)] = player
                self._b[tuple(c)] = player

            return len(toflank)


    def legalmoves(self, player):
        """
        Returns a list of all legal moves for player (integer: 1 or 2)
        Raises a ValueError if player is not known
        """

        lett = "ABCDEFGH"
        numb = "12345678"
        moves = []

        # go through the board and check whether the coordinate is legal or not
        for i in range(8):
            for j in range(8):
                if self._b[i,j] == 0:
                    try:
                        n = self.place(f"{lett[i]}{numb[j]}", player, flank = False)
                    except ValueError:
                        # illegal, will not add to the list
                        pass
                    else:
                        if n > 0:
                            moves.append(f"{lett[i]}{numb[j]}")
        return moves


    def __repr__(self):
        """String representation showing the current state of the board"""

        marker = {0: ' ', 1: '@', 2: 'O'}
        lett = "ABCDEFGH"
        bstr =   "    1   2   3   4   5   6   7   8\n"\
                +"  +---+---+---+---+---+---+---+---+\n"
        for i in range(8):
            bstr += lett[i] + " | "
            for j in range(8):
                bstr += marker[self._b[(i,j)]] + " | "
            bstr += "\n"
            bstr += "  +---+---+---+---+---+---+---+---+\n"

        return bstr
