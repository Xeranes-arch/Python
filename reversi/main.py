from Board import Board
import numpy as np
import sys


def main():
    board = Board()
    
    while True:
        legal = np.zeros_like(board.grid, dtype=bool)
        for i in range(8):
            for j in range(8):
                board.pos = (i,j)
                
                if board.grid[board.pos] == 0:
                    legal[i,j] = board.would_capture()
        
        # No legal move for player. Skips player.
        if not legal.any():

            # If reached twice without making a move, game ends.
            if end_flag:
                board.process_output()
                print(board.grid_p)
                if board.get_score() > 32:
                    winner = board.current_player
                else:
                    winner = board.inv()
                
                # Win message
                print("Winner is: Player", winner)
                print("Score of Player", board.current_player, "is:", board.get_score())
                board.current_player = board.inv()
                print("Score of Player", board.inv(),
                      "is:", board.get_score())
                
                sys.exit()

            # Skipping Player
            print("No legal move for Player " + str(board.current_player) + ".")
            board.current_player = board.inv()

            end_flag = True
            continue

        # Other Player after skip can play -> don't end game
        end_flag = False

        # One Turn
        try:
            # Preturn print
            board.process_output()
            print("Player " + str(board.current_player) + " it's your turn!")
            print(board.grid_p)

            # Manual Player
            #x = int(input("Give input x: ")) - 1
            #y = int(input("Give input y: ")) - 1

            # Auto Player
            while True:
                x = np.random.randint(1,9) - 1
                y = np.random.randint(1,9) - 1
                if legal[y,x]:
                    break
            
            # Make move
            board.pos = (y, x)
            if board.would_capture():
                board.capture()
                board.current_player = board.inv()
            else:
                print("-------------------------------\nInvalid move.\n-------------------------------")

        except KeyboardInterrupt:
            print("\nShut down.")
            break
        except ValueError:
            print(
                "-------------------------------\nThat's not a valid input.\n-------------------------------")


if __name__ == "__main__":
    main()
