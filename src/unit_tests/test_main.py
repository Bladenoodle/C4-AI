"""This module is for testing the the function iterative_deepening"""

import time
from main import iterative_deepening
from connect_4 import create_board, make_move

def test_iterative_deepening_stops_in_time():
    """Check that time limit is accomplished"""
    board = create_board()
    start = time.time()
    (result, depth) = iterative_deepening(board, 0.5, True, None)
    stop_time = time.time() - start
    assert stop_time < 1.0
    assert isinstance(result, tuple)
    assert isinstance(depth, int)

def test_iterative_deepening_detects_win_immediately():
    """Check that instant return if game ended"""
    board = create_board()
    for i in range(4):
        make_move(board, i, 1)
    result, _ = iterative_deepening(board, 1, True, (3, 5))
    assert result == (None, None)

def test_iterative_deepening_detects_win_in_one():
    """Check that finds win in one"""
    board = create_board()
    for i in range(3):
        make_move(board, i, 1)
    result, _ = iterative_deepening(board, 1, True, (2, 5))
    assert result[0] == 100000
