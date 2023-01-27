from othgame.game import Game
from othgame.player import Player

import sys

def main():

    player1 = Player(1)
    player2 = Player(2)
    game = Game(player1, player2)
    while True:
        try:
            p = int(input("How many Players should be human? (0-2)\n"))
        except ValueError:
            print("That's not a valid input.")
            continue

        if p == 1:
            player1.human()
        elif p == 2:
            player1.human()
            player2.human()

        game.run()

        #TODO Display HallofFame
        again = input("Would you like to play again? (y/n)\n")
        if again != "y":
            break
        elif again != "n":
            sys.exit()


if __name__ == "__main__":
    main()