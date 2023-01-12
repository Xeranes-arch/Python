import tictactoe
import sys
sys.modules["tictactoe"] = tictactoe


from tictactoe import Game

def main():
    """main:
    Query for names.
    Query for a stats file name. If none is entered, use "stats.json" as a default
    if a TimeoutError occurs, exit the program using sys.exit(0).
    if a EOFError occures, exit the program using sys.exit(0).
    """
    name_1 = input("Name for Player1:")
    name_2 = input("Name for Player2:")
    filename = "stats.json"
    new = input("filename of HallofFame:")
    if not new == "":
        filename = new
    game = Game(name_1, name_2, filename)
    while True:
        try:
            print(game.board)
            Game.make_move(game)
        except TimeoutError:
            sys.exit(0)
        except EOFError:
            sys.exit(0)



if __name__ == "__main__":
    main()
