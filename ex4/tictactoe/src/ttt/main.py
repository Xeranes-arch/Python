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
    name_1 = "Alice"
    name_2 = "Bob"
    filename = "stats.json"
    a = input("Name for Player1:")
    if not a == "":
        name_1 = a
    b = input("Name for Player2:")
    if not b == "":
        name_2 = b
    new = input("Filename of HallofFame:")
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
