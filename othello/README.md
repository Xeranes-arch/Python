# Othello
Othello is a two-player game that is played on a 8 x 8 checker board with discs that are white on one side and black on the other side. The game begins with four disks placed in a square in the middle of the grid, two facing light-side-up, two dark-side-up, so that the same-colored disks are on a diagonal. The goal of the game is to have more discs be of your colour than your oponent.
 
Rules:
-
- A piece must be placed so that there exists at least one straight (horizontal, vertical, or diagonal) occupied line between the new piece and another one of its kind, with one or more contiguous enemy pieces between them.
- Pieces "surrounded" in such a manner are flipped to their dark side.
- Play alternates every turn.
- When there are no legal turns for a player he is skipped
- If neither player has a legal turn, the game ends.

Features:
-
- The user may choose how many human players partake in the game
- Set player names
- Once a game has been won and if a filename was specified via docopt, the game will extend the Hall of Fame by one entry, print and save it. If the specified file doesn't yet exist, it is created.
- Writes all time stats in all_time.json 
- Prompts user whether they wish to play again
- Takes docopt options as shown below
---
Usage:

othello.py [--n=number_of_human_players] [--f=halloffame_filename]