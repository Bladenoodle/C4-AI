"""This module is for testing the the functions in file connect_4.py"""

import pytest
from connect_4 import (
    create_board, make_move, check_win, check_draw,
    heuristic, minimax
)

# Board functionalities
def test_make_move():
    """Test making a valid move"""
    board = create_board()
    last_move = make_move(board, 3, 1)
    assert last_move == (3, 5)
    assert board[5][3] == 1

def test_make_move_invalid_column_raises():
    """Test if invalid column raises a value error"""
    board = create_board()
    with pytest.raises(ValueError):
        make_move(board, 8, 1)

def test_make_move_full_column_raises():
    """Test if making a move to full column raises value error"""
    board = create_board()
    for _ in range(6):
        make_move(board, 0, 1)
    with pytest.raises(ValueError):
        make_move(board, 0, 1)

# Check win correctness

def test_check_win_horizontal():
    """Check if side 1 won horizontally"""
    board = create_board()
    for i in range(4):
        make_move(board, i, 1)
    assert check_win(board, (3, 5))

def test_check_win_vertical():
    """Check if side 1 won vertically"""
    board = create_board()
    for _ in range(4):
        last = make_move(board, 0, 1)
    assert check_win(board, last)

def test_check_draw_true_when_full():
    """Check if board is full"""
    board = create_board()

    for y in range(6):
        for x in range(7):
            board[y][x] = (x + y) % 2 + 1
    assert check_draw(board)

# Heuristic correctness

def test_heuristic_favors_center():
    """Check that heuristic funtion favors center"""
    board_center = create_board()
    board_side = create_board()
    make_move(board_center, 3, 1)
    make_move(board_side, 0, 1)
    assert heuristic(board_center) > heuristic(board_side)

def test_heuristic_value():
    """Checks that heuristic function returns right values"""
    board1 = create_board()
    board2 = create_board()
    make_move(board1, 3, 1)
    make_move(board2, 3, 2)
    assert heuristic(board1) > 0
    assert heuristic(board2) < 0

# Minimax correctness

def test_minimax_win_self():
    """Check can minimax spot win in 1 for self"""
    board = create_board()
    for c in range(3):
        make_move(board, c, 1)
    _, best_move = minimax(board, 3, float('-inf'), float('inf'), True, {}, (2,5))
    assert best_move == 3

def test_minimax_win_opponent():
    """Check can minimax spot win in 1 for enemy"""
    board = create_board()
    for c in range(3):
        make_move(board, c, 2)
    _, best_move = minimax(board, 3, float('-inf'), float('inf'), True, {}, (2,5))
    assert best_move == 3

def test_minimax_return_when_depth_0():
    """Check that minimax returns right value at depth 0"""
    board = create_board()
    make_move(board, 3, 1)
    _, best_move = minimax(board, 0, float('-inf'), float('inf'), True, {}, (3,5))
    assert best_move is None
