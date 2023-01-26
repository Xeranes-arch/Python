import pytest

from ttt import tictactoe
from ttt.tictactoe import Player

def test_version():
    """test TicTacToe version number"""
    assert tictactoe.__version__ == "0.1.0"


@pytest.fixture
def player():
    """return a testing player"""
    player = Player("Alice", "X")
    return player


def test_has_name(player):
    assert hasattr(player, "name")


def test_has_marker(player):
    assert hasattr(player, "marker")


def test__str__(player):
    """assert that Player has the name as a __str__ representation"""
    assert player.__str__() == "Alice"

def test_returns_name(player):
    assert player.name == "Alice"

def test_empty_name_raises_error(player):
    try:
        player.name = ""
        pytest.fail("Player class allows setting an empty name")
    except ValueError:
        assert True

def test_returns_marker(player):
    assert player.marker == "X"

def test_illegal_marker_raises_error(player):
    for marker in ["A", "1", "Y", "C", ""]:
        try:
            player.marker = marker
            pytest.fail(f"Player class allowed use of illegal marker \"{marker}\"")
        except ValueError:
            continue
    assert True

def test_marker_setter_case_insensitive(player):
    for marker in ["X", "x", "O", "o"]:
        try:
            player.marker = marker
            assert player.marker == marker.upper()
        except ValueError:
            pytest.fail(f"Player class did not accept legal marker \"{marker}\"")

