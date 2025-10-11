"""Module for testing minimax algorithm with 5 hard puzzles"""

from connect_4 import minimax

def test_depth_calculation():
    """Testing the minimax with win in 5 puzzles.
       The algorithm should return 100 000 with depth 9.
       Depth 9 because the turns starts with self,
       and the win should occur in 5 own moves + 4 opponent moves.
       Heuristic value of 100 000 means that it finds a win at max depth"""
    puzzles = [
        ([
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0],
            [0, 1, 2, 2, 1, 2, 0],
            [0, 1, 1, 2, 2, 1, 2],
        ], (2,1)),
        ([
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [1, 1, 2, 2, 1, 1, 2],
            [2, 1, 2, 1, 2, 1, 2],
        ], (2,1)),

        ([
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 1, 0, 2, 0],
            [2, 0, 1, 2, 0, 2, 0],
            [1, 2, 2, 2, 1, 1, 0],
        ], (5,2)),

        ([
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 2, 0, 0, 2, 2, 0],
            [0, 1, 0, 0, 1, 1, 0],
            [1, 1, 0, 0, 1, 1, 0],
            [2, 2, 0, 0, 2, 2, 0],
        ], (1,3)),

        ([
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 2],
            [0, 2, 2, 0, 0, 0, 1],
            [0, 2, 1, 0, 1, 1, 2],
            [0, 1, 2, 0, 2, 1, 1],
        ], (2,2))
    ]
    for board, last_move in puzzles:
        assert 100000 == minimax(board, 9, float("-inf"), float("inf"), True, {}, last_move)[0]
