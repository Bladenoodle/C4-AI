"""Module providing a Connect Four playing AI with minimax."""

from connect_4 import ConnectFour

def minimax(
            game: ConnectFour,
            depth: int,
            is_maximizing:bool,
            alpha=None,
            beta=None,
            original_depth=None
            ):
    """
    Minimax algorithm that calculates a move from a given position for a given side.
    """
    if original_depth is None:
        original_depth = depth
    if alpha is None:
        alpha = float("-inf")
    if beta is None:
        beta = float("inf")

    if depth == 0 or game.heuristic() == float("inf") or game.heuristic() == float("-inf"):
        return game.heuristic()

    if is_maximizing:
        best_val = float("-inf")
        best_move = None

        for move in game.valid_moves():
            game_copy = ConnectFour(turn=game.turn)
            game_copy.clone_position(game)
            game_copy.make_move(move)
            new_val = minimax(game_copy, depth - 1, False, alpha, beta, original_depth)
            if best_val < new_val:
                best_val = new_val
                best_move = move
            alpha = max(alpha, new_val)
            if beta <= alpha:
                break
        if depth < original_depth:
            return best_val
        print(best_val)
        return best_move if best_move else game.valid_moves()[0]

    best_val = float("inf")
    best_move = None

    for move in game.valid_moves():
        game_copy = ConnectFour(turn=game.turn)
        game_copy.clone_position(game)
        game_copy.make_move(move)
        new_val = minimax(game_copy, depth - 1, True, alpha, beta, original_depth)

        if best_val > new_val:
            best_val = new_val
            best_move = move
        beta = min(beta, new_val)
        if beta <= alpha:
            break
    if depth < original_depth:
        return best_val
    print(best_val)
    return best_move if best_move else game.valid_moves()[0]
