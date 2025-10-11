"""Module for testing a full game played by AIs"""

from random import uniform
from main import iterative_deepening
from connect_4 import create_board, make_move, check_win, check_draw


def test_end_to_end():
    """Run a game with two AI playing each other win a semi-random time limit"""
    board = create_board()

    cal_time1 = uniform(0.1,1)
    cal_time2 = uniform(0.1,1)
    last_move = None

    for _ in range(21): # Maximum amount of moves turns, because 21 turns = 42 = 6x7 moves
        best, _ = iterative_deepening(board, cal_time1, True, last_move)
        _, best_move = best
        assert best_move is not None and 0 <= best_move < 7
        last_move = make_move(board, best_move, 1)
        if check_win(board, last_move) or check_draw(board):
            break

        best, _ = iterative_deepening(board, cal_time2, False, last_move)
        _, best_move = best
        assert best_move is not None and 0 <= best_move < 7
        last_move = make_move(board, best_move, 2)
        if check_win(board, last_move) or check_draw(board):
            break
    else:
        assert False, "Game did not terminate within 42 moves"
