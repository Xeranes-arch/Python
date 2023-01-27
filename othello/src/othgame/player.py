import time
import random

class Player():

    def __init__(self, nr, p=2):
        self.nr = nr
        self.mode = 2
        self.name = ""
        
    def human(self):
        """Make player human. Is Computer by default."""

        self.mode = 1
        print("Player" + str(self.nr))
        self.name = input("Please give a name for the Player:")


    def __repr__(self):
        """String representation of the Player."""

        # Human player represented by their name
        if self.mode == 1:
            return self.name
        
        # Computer player represented by their number
        if self.mode == 2:
            return "Player" + str(self.nr)
    
    def make_move(self, legal):
        """
        Prompts player to make a move and returns the chosen position.
        """

        # Human move
        if self.mode == 1:
            while True:
                print("Where would you like to place your disc?\nYour choices are:", legal)
                pos = input()
                if pos in legal:
                    break
                print("That's not a legal move.")

        # Bot move
        else:

            # Picks move from legal list and deletes brackets
            time.sleep(1)
            pos = (str(random.sample(legal, k = 1))[2:-2])
            print(pos)
            time.sleep(1)
        
        return pos