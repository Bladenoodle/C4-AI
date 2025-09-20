"""Module providing a class ConnectFour"""

class ConnectFour:
    """ A class for connect 4 game, which has 7 rows and 6 columns.
    The cells will contain either 0 (empty), 1 (player 1's token) or 2 (player 2's token).
    """

    def __init__(self, board=None, turn=None, last=None, empty=None, ps1=None, ps2=None):
        """ initializing board and tracking turns"""
        self.turn = turn if turn else 1
        self.last = last

        if board:
            self.board = board
            if empty:
                self.empty = empty
            else:
                self.empty = set()
                for y, row in enumerate(self.board[::-1]):
                    for x, cell in enumerate(row):
                        if cell == 0:
                            self.empty.add((x, y))
            self.ps1 = ps1 if ps1 else set()
            self.ps2 = ps2 if ps2 else set()

        else:
            self.board = [[0 for i in range(7)] for i in range(6)]
            if empty:
                self.empty = empty
            else:
                self.empty = set()
                for y, row in enumerate(self.board[::-1]):
                    for x, cell in enumerate(row):
                        if cell == 0:
                            self.empty.add((x, y))
            self.ps1 = ps1 if ps1 else set()
            self.ps2 = ps2 if ps2 else set()

    def print_board(self):
        """
        Pretty prints the current board.
        If a player has won, outlines the winning 4.
        """
        # print("")
        # for row in self.board:
        #     print(row)
        # print("")
        print()

        win_coords = set()
        for player in [1, 2]:
            ps = {(x, y) for y, row in enumerate(self.board)
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

        print("  " + " ".join(f" {i+1} " for i in range(len(self.board[0]))))
        print(" +" + "---+" * len(self.board[0]))

        for y, row in enumerate(self.board):
            row_str = " |"
            for x, cell in enumerate(row):
                cell_char = self._cell_repr(cell)
                if (x, y) in win_coords:
                    cell_char = f"[{cell_char}]"
                else:
                    cell_char = f" {cell_char} "
                row_str += cell_char + "|"
            print(row_str)
            print(" +" + "---+" * len(self.board[0]))
        print()

    def _cell_repr(self, cell):
        """Helper to visualize a cell: 0=empty, 1=player, 2=opponent."""
        if cell == 0:
            return " "
        if cell == 1:
            return "X"
        return "O"

    def make_move(self, col):
        """ Makes a move for the player whose move it is with a given column parameter"""
        if self.board[0][col] != 0:
            raise ValueError
        for y, row in enumerate(self.board[::-1]):
            if row[col] == 0:
                row[col] = self.turn
                new = (col, y)
                if self.turn == 1:
                    self.ps1.add(new)
                else:
                    self.ps2.add(new)
                self.turn = self.turn % 2 + 1
                self.last = new
                self.empty.remove(new)
                break

    def clone(self):
        """Return a deep clone of the game state."""
        return (
            [row[:] for row in self.board],
            self.turn,
            self.last,
            self.empty.copy(),
            self.ps1.copy(),
            self.ps2.copy()
        )

    def clone_position(self, board):
        """ Function for the receiving part when cloning a game"""
        self.board, self.turn, self.last, self.empty, self.ps1, self.ps2 = board.clone()

    def valid_moves(self):
        """ Returns a list of valid moves to choose from"""
        moves = [x for x, val in enumerate(self.board[0]) if val == 0]
        return moves

    def valid_concrete_moves(self):
        """
        Returns a list of (row, col) coordinates where a move can be made.
        """
        coords = []
        for col in range(len(self.board[0])):
            for row in range(len(self.board)):
                if self.board[row][col] != 0:
                    if row > 0:
                        coords.append((5 - (row - 5), col))
                    break
            else:
                coords.append((5 - (len(self.board) - 1), col))
        return coords

    def check_win_helper(self, ps):
        """ Checks win for a given side.
        NEEDS TO BE CALLED BY: check_win OR heuristic.
        """
        win_patterns = [
            [(1, 1), (2, 2), (3, 3)],  # diagonal right-down
            [(1, 0), (2, 0), (3, 0)],  # horizontal right
            [(0, 1), (0, 2), (0, 3)],  # vertical down
            [(-1, 1), (-2, 2), (-3, 3)]  # diagonal left-down
        ]
        for x, y in ps:
            for pattern in win_patterns:
                if all((x+dx, y+dy) in ps for dx, dy in pattern):
                    return True
        return False

    def check_win(self, side):
        """Called to check if a given side has won"""
        ps = {(x, y) for y, row in enumerate(self.board)
              for x, cell in enumerate(row) if cell == side}
        return self.check_win_helper(ps)

    def heuristic_helper(self, ps1, ps2, xy, direction):
        """Checks the heuristic for a certain side and angle of line.
        NEEDS TO BE CALLED BY: heuristic
        """
        x, y = xy
        dx, dy = direction

        def is_blocked(coord):
            cx, cy = coord
            if not (0 <= cx < 7 and 0 <= cy < 6):
                return True  # Out of range
            return coord in ps2  # Blocked if opponent piece

        value = 0
        prev = (x - dx, y - dy)

        if prev not in ps1:  # Skip if already checked
            for i in range(1, 4):
                new = (x + i * dx, y + i * dy)
                if new not in ps1:
                    if is_blocked(new) and is_blocked(prev):
                        value = 0
                    elif is_blocked(new) or is_blocked(prev):
                        value //= 2
                    elif new in self.valid_concrete_moves() and prev in self.valid_concrete_moves():
                        if value == 4:
                            value = float("inf")
                        else:
                            value *= 3
                    elif new in self.valid_concrete_moves() or prev in self.valid_concrete_moves():
                        value *= 2
                value += 2
        return value

    def heuristic(self):
        """Calculates heuristic value for a side in a position"""
        ps1 = {(x, y) for y, row in enumerate(self.board)
               for x, cell in enumerate(row) if cell == 1}
        ps2 = {(x, y) for y, row in enumerate(self.board)
               for x, cell in enumerate(row) if cell == 2}

        if self.check_win_helper(ps1):
            return float("inf")
        if self.check_win_helper(ps2):
            return float("-inf")

        heuristic_value = 0
        directions = [(1, 0), (0, 1), (1, 1), (-1, 1)]

        for x, y in ps1:
            heuristic_value += sum(
                self.heuristic_helper(ps1, ps2, (x, y),  d) for d in directions
            )

        for x, y in ps2:
            heuristic_value -= sum(
                self.heuristic_helper(ps2, ps1, (x, y), d) for d in directions
            )

        return heuristic_value


def play_game():
    """ Used to play a game to test how class ConnectFour works"""
    game1 = ConnectFour()
    side = 2  # Setup bool to determine whose turn

    while not game1.check_win(1) and not game1.check_win(2):  # Game loop
        move = None
        side = side % 2 + 1
        invalid_move = False
        if not game1.valid_moves():
            break
        game1.print_board()
        print("Valid moves: ", end="")
        print(*game1.valid_moves(), sep=", ")
        while move not in game1.valid_moves():
            if invalid_move:
                move = input("Invalid move! Choose another move: ")
            else:
                print(f"Player {side}'s turn")
                move = input("Make a move: ")
            try:
                move = int(move)
            except ValueError:
                invalid_move = True
                continue
            invalid_move = True
        game1.make_move(move)

    if game1.check_win(1):
        game1.print_board()
        print("Player 1 won!")
    elif game1.check_win(2):
        game1.print_board()
        print("Player 2 won!")
    else:
        game1.print_board()
        print("Game Tied")
