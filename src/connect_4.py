"""Module providing a connect four game and minimax algorithm solving it."""

ROWS, COLS = 6, 7

def create_board():
    """Return a new empty 6x7 Connect Four board as a 2D list filled with 0."""
    return [[0 for _ in range(COLS)] for _ in range(ROWS)]

def check_draw(board):
    """Return True if no more valid moves are available (board is full)."""
    return len(valid_columns(board)) == 0


def print_board(board):
    """
    Pretty-print the current board state.
    If a player has won, highlight the winning 4-in-a-row in brackets.
    """
    print()

    win_coords = set()
    for player in [1, 2]:
        ps = {(x, y) for y, row in enumerate(board)
              for x, cell in enumerate(row) if cell == player}
        for x, y in ps:
            win_patterns = [
                [(1, 1), (2, 2), (3, 3)],
                [(1, 0), (2, 0), (3, 0)],
                [(0, 1), (0, 2), (0, 3)],
                [(-1, 1), (-2, 2), (-3, 3)]
            ]
            for pattern in win_patterns:
                coords = [(x + dx, y + dy) for dx, dy in pattern]
                if all(c in ps for c in coords):
                    win_coords = set([(x, y)] + coords)
                    break
            if win_coords:
                break
        if win_coords:
            break

    print("  " + " ".join(f" {i+1} " for i in range(len(board[0]))))
    print(" +" + "---+" * len(board[0]))

    for y, row in enumerate(board):
        row_str = " |"
        for x, cell in enumerate(row):
            cell_char = cell_repr(cell)
            if (x, y) in win_coords:
                cell_char = f"[{cell_char}]"
            else:
                cell_char = f" {cell_char} "
            row_str += cell_char + "|"
        print(row_str)
        print(" +" + "---+" * len(board[0]))
    print()

def cell_repr(cell):
    """Return a printable representation of a board cell: 0=' ', 1='X', 2='O'."""
    if cell == 0:
        return " "
    if cell == 1:
        return "X"
    return "O"

def make_move(board, col, player):
    """
    Drop a piece into column `col` for `player`.
    Returns the (x, y) coordinates of the placed piece.
    Raises ValueError if column is invalid or full.
    """
    if not 0 <= col < COLS:
        raise ValueError("Column out of range")
    if board[0][col] != 0:
        raise ValueError("Column is full")
    # Find lowest empty row (from bottom up)
    for y in range(ROWS - 1, -1, -1):
        if board[y][col] == 0:
            board[y][col] = player
            return (col, y)
    raise ValueError("No space in column")


def valid_columns(board):
    """Return a list of playable column indices."""
    return [x for x in range(COLS) if board[0][x] == 0]


def in_bounds(x, y):
    """Return True if coordinates (x, y) are within the board."""
    return 0 <= x < COLS and 0 <= y < ROWS


def check_win(board, last_move):
    """
    Return True if "last_move" (x, y) resulted in a win.
    Checks horizontal, vertical, and diagonal 4-in-a-rows.
    """
    if last_move is None:
        return False
    x0, y0 = last_move
    player = board[y0][x0]
    if player == 0:
        return False

    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
    for dx, dy in directions:
        count = 1
        # forward
        x, y = x0 + dx, y0 + dy
        while in_bounds(x, y) and board[y][x] == player:
            count += 1
            x += dx
            y += dy
        # backward
        x, y = x0 - dx, y0 - dy
        while in_bounds(x, y) and board[y][x] == player:
            count += 1
            x -= dx
            y -= dy
        if count >= 4:
            return True
    return False

def heuristic_helper(board, xy, direction, player):
    """
    Score a line segment starting at xy in given direction for player.
    Avoids double-counting by only scoring if previous cell is not player's.
    Rules:
      - Both ends blocked → 0
      - One end blocked   → lower base value
      - Both ends open    → higher base value
    """
    opponent = 3 - player
    x, y = xy
    dx, dy = direction

    def is_blocked(cx, cy):
        return not in_bounds(cx, cy) or board[cy][cx] == opponent

    # Avoid double counting
    prevx, prevy = x - dx, y - dy
    if in_bounds(prevx, prevy) and board[prevy][prevx] == player:
        return 0

    # Count consecutive player's pieces
    count = 1
    for i in range(1, 4):
        nx, ny = x + i * dx, y + i * dy
        if not in_bounds(nx, ny) or board[ny][nx] != player:
            break
        count += 1

    # Blocking check
    back_blocked = is_blocked(prevx, prevy)
    endx, endy = x + count * dx, y + count * dy
    fwd_blocked = is_blocked(endx, endy)

    if back_blocked and fwd_blocked:
        return 0
    if back_blocked or fwd_blocked:
        if count == 2:
            return 2
        if count == 3:
            return 10
        return 0
    if count == 2:
        return 20
    if count == 3:
        return 100
    return 0


def heuristic(board):
    """
    Calculate heuristic score of board.
    Positive = good for Player 1 (X), negative = good for Player 2 (O).
    Combines positional table values and run-based values.
    """
    heuristic_table = [
        [3, 4, 5, 7, 5, 4, 3],
        [4, 6, 8, 10, 8, 6, 4],
        [5, 8, 11, 13, 11, 8, 5],
        [5, 8, 11, 13, 11, 8, 5],
        [4, 6, 8, 10, 8, 6, 4],
        [3, 4, 5, 7, 5, 4, 3],
    ]

    score = 0
    directions = [(1, 0), (0, 1), (1, 1), (-1, 1)]
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if cell == 1:
                score += sum(heuristic_helper(board, (x, y), d, 1) for d in directions)
                score += heuristic_table[y][x]
            elif cell == 2:
                score -= sum(heuristic_helper(board, (x, y), d, 2) for d in directions)
                score -= heuristic_table[y][x]
    return score


def clone_board(board):
    """Return a deep copy of the board."""
    return [row[:] for row in board]


def minimax(board, depth, alpha, beta, maximizing, memory, last_move=None):
    """
    Minimax with alpha-beta pruning and transposition table.
    Returns (score, move).
    """
    str_board = str(board)
    if last_move is not None and check_win(board, last_move):
        winner = board[last_move[1]][last_move[0]]
        return (100000 + depth, None) if winner == 1 else (-100000 - depth, None)

    if depth == 0:
        return heuristic(board), None

    check_order = [3, 2, 4, 1, 5, 0, 6]  # center-first ordering
    valid_moves = [col for col in check_order if board[0][col] == 0]
    if not valid_moves:
        return 0, None

    if str_board in memory:
        _, prev_best = memory[str_board]
        if prev_best in valid_moves:
            valid_moves.remove(prev_best)
            valid_moves.insert(0, prev_best)

    if maximizing:
        best_eval, best_move = float("-inf"), None
        for col in valid_moves:
            new_board = clone_board(board)
            new_last = make_move(new_board, col, 1)
            child_eval, _ = minimax(new_board, depth - 1, alpha, beta, False, memory, new_last)
            if child_eval > best_eval:
                best_eval, best_move = child_eval, col
                alpha = max(alpha, best_eval)
            if beta <= alpha:
                break
        memory[str_board] = (best_eval, best_move)
        return best_eval, best_move

    best_eval, best_move = float("inf"), None
    for col in valid_moves:
        new_board = clone_board(board)
        new_last = make_move(new_board, col, 2)
        child_eval, _ = minimax(new_board, depth - 1, alpha, beta, True, memory, new_last)
        if child_eval < best_eval:
            best_eval, best_move = child_eval, col
            beta = min(beta, best_eval)
        if beta <= alpha:
            break
    memory[str_board] = (best_eval, best_move)
    return best_eval, best_move
