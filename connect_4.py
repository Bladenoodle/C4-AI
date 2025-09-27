"""Module providing a connect four game and minimax algorithm solving it"""

ROWS, COLS = 6, 7

def create_board():
    return [[0 for _ in range(COLS)] for _ in range(ROWS)]

def check_draw(board):
    return True if valid_columns(board) is None else False

def print_board(board):
    """
    Pretty prints the current board.
    If a player has won, outlines the winning 4.
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
    """Helper to visualize a cell: 0=empty, 1=player, 2=opponent."""
    if cell == 0:
        return " "
    if cell == 1:
        return "X"
    return "O"

def make_move(board, col, player):
    """Drop a piece into column "col". Returns (x, y) in board indices (top-left origin)."""
    if not (0 <= col < COLS):
        raise ValueError("Column out of range")
    if board[0][col] != 0:
        raise ValueError("Column is full")
    # Find lowest empty row (from bottom up)
    for y in range(ROWS - 1, -1, -1):
        if board[y][col] == 0:
            board[y][col] = player
            return (col, y)
    # Shouldn't reach here due to the top check
    raise ValueError("No space in column")

def valid_columns(board):
    """Return list of column indices that are playable."""
    valid = []
    for x in range(COLS):
        if board[0][x] == 0:
            valid.append(x)
    return valid

def in_bounds(x, y):
    """Return if given x and y are possible."""
    return 0 <= x < COLS and 0 <= y < ROWS

def check_win(board, last_move):
    """Check win that includes the last move using 4 directions and bounds checks."""
    if last_move is None:
        return False
    x0, y0 = last_move
    player = board[y0][x0]
    if player == 0:
        return False

    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]  # right, down, diag-down-right, diag-up-right
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
    Score a run that starts at xy in the given direction for player,
    without double-counting (we only score if the previous cell is not player's).
    Blocking rules:
      - both ends blocked -> 0
      - one end blocked  -> half (here: lower base)
      - both open        -> full base
    """
    opponent = 3 - player
    x, y = xy
    dx, dy = direction

    def is_blocked(cx, cy):
        if not in_bounds(cx, cy):
            return True
        return board[cy][cx] == opponent

    # Avoid double counting: only score if previous cell in line is NOT player's
    prevx, prevy = x - dx, y - dy
    if in_bounds(prevx, prevy) and board[prevy][prevx] == player:
        return 0

    # Count consecutive player's pieces forward (including (x,y))
    count = 1
    for i in range(1, 4):
        nx, ny = x + i*dx, y + i*dy
        if not in_bounds(nx, ny):
            break
        if board[ny][nx] == player:
            count += 1
        else:
            break

    # Determine blocking at both ends of the run
    back_blocked = is_blocked(prevx, prevy)
    endx, endy = x + count*dx, y + count*dy
    fwd_blocked  = is_blocked(endx, endy)

    if back_blocked and fwd_blocked:
        return 0

    if back_blocked or fwd_blocked:
        if count == 1:
            base = 0
        elif count == 2:
            base = 2     # semi-open 2
        else:
            base = 20    # semi-open 3
    else:
        if count == 1:
            base = 0
        elif count == 2:
            base = 10    # open 2
        elif count == 3:
            base = 50   # open 3
        else:
            base = 0
    return base

def heuristic(board):
    """Calculates heuristic value for the position."""
    heuristic_table = [
        [3, 4, 5,  7, 5, 4, 3],
        [4, 6, 8, 10, 8, 6, 4],
        [5, 8,11, 13,11, 8, 5],
        [5, 8,11, 13,11, 8, 5],
        [4, 6, 8, 10, 8, 6, 4],
        [3, 4, 5,  7, 5, 4, 3],
    ]

    score = 0
    directions = [(1, 0), (0, 1), (1, 1), (-1, 1)]
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if cell == 1:
                # runs
                score += sum(heuristic_helper(board, (x, y), d, 1) for d in directions)
                score += heuristic_table[y][x]

            elif cell == 2:
                score -= sum(heuristic_helper(board, (x, y), d, 2) for d in directions)
                score -= heuristic_table[y][x]
    return score

def clone_board(board):
    return [row[:] for row in board]

def minimax(board, depth, alpha, beta, maximizing, last_move=None):
    """
    Returns (score, move) -> move is a column index or None.
    Terminal cases:
      - win (from last_move) -> heuristic(board, last_move)
      - no valid moves       -> 0 (draw)
      - depth == 0           -> heuristic(board, last_move)
    """

    if last_move is not None and check_win(board, last_move):
        winner = board[last_move[1]][last_move[0]]
        if winner == 1:
            return 100000 + depth, None # add depth to choose the fastest win
        else:
            return -100000 - depth, None

    if depth == 0:
        return heuristic(board), None
    check_order = [3, 2, 4, 1, 5, 0, 6] # checking from middle gives a better chance to save time by pruning
    valid_moves = [col for col in check_order if board[0][col] == 0]
    if not valid_moves:
        return 0, None
    # maximizing player
    if maximizing:
        best_eval = float("-inf")
        best_move = None
        for col in valid_moves:
            new_board = clone_board(board)
            last_move = make_move(new_board, col, 1)
            child_eval, _ = minimax(new_board, depth - 1, alpha, beta, False, last_move)
            if child_eval > best_eval:
                best_eval, best_move = child_eval, col
                alpha = max(alpha, best_eval) # only check when best move is changed
            if beta <= alpha:
                break
        return best_eval, best_move
    # minimizing player
    best_eval = float("inf")
    best_move = None
    for col in valid_moves:
        new_board = clone_board(board)
        last_move = make_move(new_board, col, 2)
        child_eval, _ = minimax(new_board, depth - 1, alpha, beta, True, last_move)
        if child_eval < best_eval:
            best_eval, best_move = child_eval, col
            beta = min(beta, best_eval)
        if beta <= alpha:
            break
    return best_eval, best_move
