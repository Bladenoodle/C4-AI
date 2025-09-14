"""Module providing a Connect Four playing AI with minimax."""

from connect_4 import ConnectFour


def minimax(game: ConnectFour, depth: int, is_maximizing: bool, original_depth: int | None = None):
    """
    Minimax algorithm that calculates a move from a given position for side 1.
    """
    if original_depth is None:
        original_depth = depth

    if depth == 0 or abs(game.heuristic()) == 10000:
        return game.heuristic()

    if is_maximizing:
        best_val = float("-inf")
        best_move = None

        for move in game.valid_moves():
            game_copy = ConnectFour()
            game_copy.insert_position(game)
            game_copy.make_move(move)
            new_val = minimax(game_copy, depth - 1, False, original_depth)
            if best_val < new_val:
                best_val = new_val
                best_move = move
        return best_val if depth < original_depth else best_move

    best_val = float("inf")
    best_move = None

    for move in game.valid_moves():
        game_copy = ConnectFour()
        game_copy.insert_position(game)
        game_copy.make_move(move)
        new_val = minimax(game_copy, depth - 1, True, original_depth)
        if best_val > new_val:
            best_val = new_val
            best_move = move
    return best_val if depth < original_depth else best_move
