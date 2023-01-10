"""Testing suite of TicTacToe - Game"""

import json
import pytest
import os

from unittest import mock
import numpy as np

from ttt import tictactoe
from ttt.tictactoe import Player
from ttt.tictactoe import Board
from ttt.tictactoe import Game

import sys
sys.modules["tictactoe"] = tictactoe

STATS= "stats.json"

@pytest.fixture
def player_1():
    """a Player of the game"""
    player = Player(name="Alice", marker="X")
    return player


@pytest.fixture
def player_2():
    """another Player of the game"""
    player = Player(name="Bob", marker="O")
    return player


@pytest.fixture
def game():
    """a game of TicTacToe"""
    return Game(name_1="Alice", name_2="Bob", statistics=STATS)

def test_has_make_move(game):
    """check that game has a method make_move"""
    assert hasattr(game, "make_move")


@pytest.fixture
def full_board():
    """a full board"""
    board = Board()
    board.grid.fill("A")
    return board

@pytest.fixture
def one_remaining():
    """A board where player X is about to win"""
    board = Board()
    board.grid = np.array([["", "", ""],["X", "", ""],["X", "", ""]])
    return board

@mock.patch("builtins.input", lambda spot: "1")
def test_detect_draw(game, full_board):
    """assert the game raises an EOFError if the board is full and noone has won"""
    game.board = full_board  # Fill the board
    game.board.grid[0][0] = ""  # remove one
    try:
        game.make_move()  # fill the last spot
        pytest.fail("Draw undetected!")
    except EOFError:
        assert True

@mock.patch("builtins.input", lambda spot: "1")
def test_play_one_round(game):
    game.make_move()
    assert game.board.grid[0, 0] == "X"
    game.board.grid[0, :2] = np.array(["", "X"])
    game.make_move()
    print(game.board.grid)
    assert np.all(game.board.grid[0, :2] == np.array(["O", "X"]))


@mock.patch("builtins.input", lambda input: "q")
def test_q_raises_eof(game):
    """test that pressing 'q' raises an EOFError"""
    try:
        game.make_move()
        pytest.fail("Pressing 'q' did not  raise an EOFError")
    except EOFError:
        assert True

@mock.patch("builtins.input", lambda spot: "1")
def test_play_writes_stats(game, one_remaining, stats=STATS):
    """checks that Game.play writes the stats to a json file"""
    try:
        game.board = one_remaining
        game.make_move()
        with open(STATS) as fn:
            stats = json.load(fn)
    except TimeoutError:
        pass # we reraise to finish the game
    except:
        pytest.fail("could not load the stats_file.")
