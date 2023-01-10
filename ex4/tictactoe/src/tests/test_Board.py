#!/bin/env python3

"""testing suite of TicTacToe - Board"""

import pytest
import numpy as np

from ttt.tictactoe import Board, __version__


def test_version():
    """tests TicTacToe version number"""
    assert __version__ == "0.1.0"


@pytest.fixture
def board():
    """return a testing board"""
    grid = Board()
    return grid


def test_has_correct_shape_and_dtype(board):
    """make sure, board has grid with correct shape and dtype (str)"""
    assert hasattr(board, "grid")
    assert board.grid.dtype == "<U1"
    assert board.grid.shape == (3, 3)


def test_initializes_empty(board):
    """board should not contain any value upon initialization"""
    assert hasattr(board, "grid")
    assert (board.grid == "").all()


def test_has_str():
    """assert that the board has an altered __str__ method"""
    board = Board()
    assert hasattr(board, "__str__")
    # Typically, an inherited __str__ method returns a string that looks like <tictactoe.Board at (memory address)>.
    # The following check will be False if the __str__ method was not overwritten.
    assert not board.__str__().startswith("<")


def test_has_place(board):
    """assert that the bord has a method that places a marker"""
    assert hasattr(board, "place")
    test_grid = np.zeros((3, 3), dtype=str)
    markers = ["X", "O"]
    for i in range(3):
        for j in range(3):
            position = 3 * i + j + 1
            m = np.random.choice(markers)
            test_grid[i, j] = m
            board.place(position, m)
    assert (test_grid == board.grid).all()


def test_place_has_markers(board):
    """assert, one can put various markers on the board"""
    try:
        board.place(1, marker="X")
        board.place(2, marker="O")
        markers = board.grid[0, :2]
        assert all(markers == np.array(["X", "O"]))
    except TypeError:
        pytest.fail("board.place does not accept markers")


def test_place_fills_the_grid(board):
    """assert that one can fill the grid using board.place"""
    test_grid = np.array(["X" for s in range(9)]).reshape((3, 3))
    for pos in range(1, 10):
        board.place(pos, "X")
    assert (test_grid == board.grid).all()


@pytest.fixture
def full_board():
    """a full board"""
    board = Board()
    board.grid.fill("X")
    return board


def test_full_slot(full_board):
    """check that one cannot put a marker into a full slot"""
    for pos in range(1, 10):
        try:
            full_board.place(pos, "X")
            pytest.fail(f"Overflowing slot {pos} not detected")
        except ValueError:
            assert True


def test_invalid_column(board):
    """test that a ValueError is raised if the player attempts to put a marker
    in an inexistent spot.
    """
    for pos in [-1, 0, 10, 11]:
        try:
            board.place(pos, marker="X")
            pytest.fail(
                f"Invalid move not detected: Position {pos} does not exist, but the program allowed the test to place a marker there.")
        except ValueError:
            assert True


@pytest.fixture
def horizontal(board):
    """horizontal winning pattern"""
    for i in range(1, 4):
        board.place(i, "X")
    return board


@pytest.fixture
def vertical(board):
    """vertical winning pattern"""
    for i in [1, 4, 7]:
        board.place(i, "X")
    return board


@pytest.fixture
def diag_down(board):
    """down-diagonal winning pattern"""
    for pos in [1, 5, 9]:
        board.place(pos, "X")
    return board


@pytest.fixture
def diag_up(board):
    """up-diagonal winning pattern"""
    for pos in [3, 5, 7]:
        board.place(pos, "X")
    return board


def won_detected(board):
    """helper function to detect wins"""
    try:
        board.has_won()
        print(board)
        pytest.fail("Win undetected.")
    except TimeoutError:
        assert True


def test_horizontal_win_detected(horizontal):
    """test board.has_won finds a horizontal win"""
    won_detected(horizontal)


def test_vertical_win_detected(vertical):
    """test board.has_won finds a vertical win"""
    won_detected(vertical)


def test_diag_down_win_detected(diag_down):
    """test board.has_won finds a falling diagonal win"""
    won_detected(diag_down)


def test_diag_up_win_detected(diag_up):
    """test board.has_won finds a rising diagonal win"""
    print(diag_up)
    won_detected(diag_up)