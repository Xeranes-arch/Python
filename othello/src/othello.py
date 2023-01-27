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
    """Sets up the game and launches it."""

    try:
        while True:
            player1 = Player(1)
            player2 = Player(2)
            game = Game(player1, player2)

            # Establish number of human players
            if options["--n"] in ["0", "1", "2"]:
                p = options["--n"]
            elif options["--n"] == None:
                p = input("How many Players should be human? [0/1/2]\n")
                if p not in ["0", "1", "2"]:
                    print("Invalid input.")
                    continue
            else:
                print("The input for the number of players via docopt is not valid.")
                break

            # Convert the according number of players to humans
            if int(p) == 1:
                player1.human()
            elif int(p) == 2:
                player1.human()
                player2.human()

            res = game.run()
    	    
            # Declare the winner or draw
            if res[0] == False:
                print("\n>>> Hey! This is a draw. That's pretty rare actually<<<\n")
                break
            else:
                print("\n>>> The Winner is", res[0], "<<<\n\nScore is " + str(res[1]) + ":" + str(res[2]) + "\n")

            f = options["--f"]
            if f != None:
                hall_of_fame(game, res, f)

            all_time(res)

            # Play again
            while True:
                again = input("Would you like to play again? [Y/n]\n")
                if again == "y" or again == "Y":
                    break
                elif again == "n":
                    sys.exit()
                else:
                    print("Invalid input.")

    except KeyboardInterrupt:
        print("Shut down.")
        sys.exit()


def hall_of_fame(game, res, f):
    """Reads the halloffame from the specified filename and extends it."""
    halloffame = {}

    # Try to get the next game number in an existing file
    try:
        file = open(".\\scores\\" + str(f))
        halloffame = json.load(file)
        new_round = "Round " + \
            str(int(
                ((list(halloffame.keys())[-1]).split(" "))[-1]) + 1)

    # Create new first round in new file if no such file
    except FileNotFoundError:
        new_round = "Round 1"

    # Write score to HallofFame
    halloffame[new_round] = str(game.p1) + " vs. " + str(game.p2) + ": " + str(res[1]) + ":" + str(res[2])
    print("--------------------------------------------------\nHallofFame:")

    # Print HallofFame
    for key in halloffame:
        print(key, "|", halloffame[key], "\n--------------------------------------------------")
    with open(".\\scores\\" + str(f), 'w') as f:
        json.dump(halloffame, f)

def all_time(res):
    """Updates and displays the all time stats."""

    file = open(".\\scores\\all_time.json", 'r')
    all_time = json.load(file)
    
    # Highscore
    hs = int(all_time["Highscore:"])
    if max(res[1], res[2]) > hs:
        new = max(res[1], res[2])
        print("New Highscore!!!", hs, "->", new)
        hs = new
    else:
        print("Highscore:", hs)
    
    # Don't update won games when draw
    if res[1] != res[2]:
        all_time["Total won games:"] = str(int(all_time["Total won games:"]) + 1)

    print("Total won games:", all_time["Total won games:"], "\n--------------------------------------------------")

    # Write
    all_time["Highscore:"] = str(hs)
    with open(".\\scores\\all_time.json", 'w') as f:
        json.dump(all_time, f)




if __name__ == "__main__":
    options = docopt.docopt(__doc__)
    main()