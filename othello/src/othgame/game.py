from othgame.board import Board


class Game():
    """Creates and runs one game of Reversi."""

    def __init__(self, player1, player2):
        self.p1 = player1
        self.p2 = player2
        self.current_player = self.p1

    def run(self):
        """Runs one Round of Reversi."""

        board = Board()

        # One players turn
        while True:

            print("\n", board)
            
            legal = board.legalmoves(self.current_player.nr)

            # Skip when no legal moves
            if legal == []:
                print("Seems like you don't have any legal moves " + str(self.current_player) + ".")

                # End game if there are no legal moves twice in a row
                if end_flag:
                    s1 = board.ndiscs(self.p1.nr)
                    s2 = board.ndiscs(self.p2.nr)
                    return self.winner(s1,s2), s1, s2

                self.inv_player()
                end_flag = True
                continue

            end_flag = False
            print("It's your turn", self.current_player)

            pos = self.current_player.make_move(legal)
            board.place(pos, self.current_player.nr)
            self.inv_player()
    
    def inv_player(self):
        """Changes the current Player."""
        if self.current_player == self.p1:
            self.current_player = self.p2
        else:
            self.current_player = self.p1

    def winner(self, s1, s2):
        """Gets the string for the win message and the score sheet."""
        if s1 > s2:
            return 1
        elif s2 > s1:
            return 2
        else:
            return 0
