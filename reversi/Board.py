import numpy as np


class Board():

    def __init__(self):
        # Initial game state
        self.grid = np.zeros((8, 8))
        self.grid[3, 3] = 1
        self.grid[4, 4] = 1
        self.grid[3, 4] = 2
        self.grid[4, 3] = 2

        self.to_be_changed = np.zeros_like(self.grid, dtype=bool)
        self.current_player = 1
        self.pos = (0,0)
        self.grid_p = self.grid

   
    

    def would_capture(self):
        """Checks wich enemies would be captured by a given move. If none, therefore an illegal move, returns false."""

        x_dir = (-1, 0, 1)
        y_dir = (-1, 0, 1)
        back = False

        self.to_be_changed = np.zeros_like(self.grid, dtype=bool)

        for i in y_dir:
            for j in x_dir:

                # Skip directin (0,0)
                if i == 0 and j == 0:
                    continue

                # Distanz zu pos nach außen in (x,y) Richtung
                for d in range(1, 8):
                    
                    # Only when in Board boundaries.
                    if i*d + self.pos[0] >= 0 and i*d + self.pos[0] < 8 and j*d + self.pos[1] >= 0 and j*d + self.pos[1] < 8:
                        
                        
                        # Checks if cell is Enemy -> next cell in direction d
                        if self.grid[(self.pos[0] + i*d, self.pos[1] + j*d)] == self.inv():
                            continue

                        # Check if cell is empty -> next direction y,x
                        elif self.grid[(self.pos[0] + i*d, self.pos[1] + j*d)] == 0 or d == 1:
                            break

                        # Must be an ally, set all stones from pos to ally as to be captured
                        else:
                            for k in range(d + 1):
                                self.to_be_changed[(
                                    self.pos[0] + i*d - k*i, self.pos[1] + j*d - k*j)] = True
                                
        if self.to_be_changed.any():
            return True

    def capture(self):
        """Captures all enemies."""
        for i in range(8):
            for j in range(8):
                if self.to_be_changed[i, j]:
                    self.grid[i,j] = self.current_player
                    self.grid[self.pos] = self.current_player

    def inv(self):
        return int(not(self.current_player - 1)) + 1

    def end_of_game(self):
        pass

    def get_score(self):
        score = 0
        for i in range(8):
            for j in range(8):
                if self.grid[i,j] == self.current_player:
                    score += 1
        return score
            

    def process_output(self):
        """Make output pretty"""
        self.grid_p = (self.grid.astype(int)).astype(str)
        self.grid_p = np.array2string(self.grid_p, separator=' ', formatter={'str_kind': lambda grid_p: grid_p})
        self.grid_p = np.char.replace(self.grid_p, '2', (u'\u25CF'))
        self.grid_p = np.char.replace(self.grid_p, '1', (u'\u25CB'))
        self.grid_p = np.char.replace(self.grid_p,'0',(u'\u25A1'))
