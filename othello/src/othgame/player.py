import random

class Player():

    def __init__(self, nr):
        self.nr = nr
        self.mode = 2
        self.name = "Alice in superposition with Bob"
    

    @property
    def mode(self):
        return self.__mode

    @mode.setter
    def mode(self, value):
        if value in [1,2]:
            self.__mode = int(value)
        else:
            raise ValueError("Not a valid mode.")

    @property
    def name(self):
            return self.__name

    @name.setter
    def name(self, value):
        if type(value) == str and value != "":
            self.__name = value
        else:
            raise ValueError("Not a valid name.")

    @property
    def nr(self):
        return self.__nr

    @nr.setter
    def nr(self, value):
        if value in [1, 2]:
            self.__nr = int(value)
        else:
            raise ValueError("Not a valid nr.")
        

    def human(self):
        """Make player human and gives them a name. Is Computer by default."""
        self.mode = 1
        
        print("--------------------------------------------------\nPlayer" + str(self.nr))
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
        """Prompts player to make a move and returns the chosen position."""

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
            #time.sleep(1)

            # Picks move from legal list and deletes brackets
            pos = (str(random.sample(legal, k=1))[2:-2])
            print(pos)
            #time.sleep(1)
        
        return pos