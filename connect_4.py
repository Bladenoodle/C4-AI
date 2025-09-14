"""Module providing a class ConnectFour"""

class ConnectFour:
    """ A class for connect 4 game, which has 7 rows and 6 columns.
    The cells will contain either 0 (empty), 1 (player 1's token) or 2 (player 2's token).
    """

    def __init__(self):
        """ initializing board and tracking turns"""
        self.board = [[0 for i in range(7)] for i in range(6)]
        self.turn = 1

    def print_board(self):
        """Printing the current position of the board as a matrix"""
        print("")
        for i in self.board:
            print(i)
        print("")

    def make_move(self, col):
        """ Makes a move for the player whose move it is with a given column parameter"""
        if self.board[0][col] != 0:
            raise ValueError
        for i in self.board[::-1]:
            if i[col] == 0:
                i[col] = self.turn
                self.turn = self.turn % 2 + 1
                break

    def return_board(self):
        """ Function for the giving part when cloning a game"""
        return [row[:] for row in self.board]

    def insert_position(self, board):
        """ Function for the receiving part when cloning a game"""
        self.board = board.return_board()

    def valid_moves(self):
        """ Returns a list of valid moves to choose from"""
        moves = [idx for idx, val in enumerate(self.board[0]) if val == 0]
        return moves

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
                    break
                value += 2
        return value

    def heuristic(self):
        """Calculates heuristic value for a side in a position"""
        ps1 = {(x, y) for y, row in enumerate(self.board)
               for x, cell in enumerate(row) if cell == 1}
        ps2 = {(x, y) for y, row in enumerate(self.board)
               for x, cell in enumerate(row) if cell == 2}

        if self.check_win_helper(ps1):
            return 10000
        if self.check_win_helper(ps2):
            return -10000

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
