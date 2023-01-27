import pytest

from othgame.board import Board

board = Board()

def test_legalmoves_1():
    if board.legalmoves(1) == ['C5', 'D6', 'E3', 'F4']:
        return True
    
def test_legalmoves_2():
    if board.legalmoves(2) == ['C4', 'D3', 'E6', 'F5']:
        return True
    
def test_place():
    if board.place("C5", int(1)) == 2:
        return True