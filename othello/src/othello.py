"""
Othello.

Usage:
    othello.py
    othello.py [--n=number_of_human_players] [--f=halloffame_filename]

"""

from othgame.game import Game
from othgame.player import Player

import sys
import docopt
import json

def main():

    player1 = Player(1)
    player2 = Player(2)
    print(player1)
    game = Game(player1, player2)

    try:
        while True:
            print(options)

            if options["--n"] == None:
                p = input("How many Players should be human? [0/1/2]\n")
                if p not in ["0", "1", "2"]:
                    print("Invalid input.")
                    continue
            elif options["--n"] in ["0", "1", "2"]:
                p = options["--n"]
            else:
                print("The input for the number of players via docopt is not valid.")
                break

            if int(p) == 1:
                player1.human()
            elif int(p) == 2:
                player1.human()
                player2.human()

            res=game.run()
            print(res)
            
            # HallofFame
            if options["--f"] != None:
                halloffame = {}

                # Try to get the next game number in an existing
                try:
                    file = open(".\\scores\\" + str(options["--f"]))
                    halloffame = json.load(file)
                    new_round = "Round " + str(int(((list(halloffame.keys())[-1]).split(" "))[-1]) + 1)

                # Create new first round in new file
                except FileNotFoundError:
                    new_round = "Round 1"

                halloffame[new_round] = str(game.p1) + " vs. " + str(game.p2) + ": " + str(res[1]) + ":" + str(res[2])
                print(halloffame)

                with open(".\\scores\\" + str(options["--f"]), 'w') as f:
                    json.dump(halloffame, f)

            while True:
                again = input("Would you like to play again? [Y/n]\n")
                if again == "y":
                    break
                elif again == "n":
                    sys.exit()
                else:
                    print("Invalid input.")

    except KeyboardInterrupt:
        print("Shut down.")
        sys.exit()


if __name__ == "__main__":
    options = docopt.docopt(__doc__)
    main()