
from connect_4 import make_move, print_board, check_win, minimax, create_board, check_draw
import time
def play_game(side, depth):
    if side == 1:
        board = create_board()
        last_move = None
        for i in range(25):
            best_move = int(input("Make a move: ")) - 1
            last_move = make_move(board, best_move, 1)
            print_board(board)
            if check_win(board, last_move):
                print(f"1 Won on round {i+1}")
                break
            if check_draw(board):
                print("Game drawn")
                break

            score, best_move = minimax(board, depth, float("-inf"), float("inf"), False, last_move)
            last_move = make_move(board, best_move, 2)
            print(f"Player 2 calculates that the position is {-score} points for him")
            print_board(board)
            if check_win(board, last_move):
                print(f"2 Won on round {i+1}")
                break
            if check_draw(board):
                print("Game drawn")
                break
    else:
        board = create_board()
        last_move = None
        for i in range(25):
            score, best_move = minimax(board, depth, float("-inf"), float("inf"), True, last_move)
            last_move = make_move(board, best_move, 1)
            print(f"Player 1 calculates that the position is {score} points for him")
            print_board(board)
            if check_win(board, last_move):
                print(f"1 Won on round {i+1}")
                break
            if check_draw(board):
                print("Game drawn")
                break

            best_move = int(input("Make a move: ")) - 1
            last_move = make_move(board, best_move, 2)
            print_board(board)
            if check_win(board, last_move):
                print(f"2 Won on round {i+1}")
                break
            if check_draw(board):
                print("Game drawn")
                break

choice = None
print("Welcome to Connect 4")
while choice != "exit":
    print("Play against bot (play)")
    print("Setup a position for bots to play (watch)")
    choice = input("Choose a mode (play/watch/exit): ")
    while choice == "play":
        first = input("Play first? (y/n): ")
        depth = int(input("Choose enemy calculation depth: "))
        if first == "y":
            play_game(1, depth)
            choice = None
            time.sleep(1)
        if first == "n":
            play_game(2, depth)
            choice = None
            time.sleep(1)
    while choice == "watch":
        board = list(input("Insert a position of size 7x6: "))
        depth1 = int(input("Choose player 1 calculation depth: "))
        depth2 = int(input("Choose player 2 calculation depth: "))

        last_move = None
        for i in range(25):
            score, best_move = minimax(board, depth1, float("-inf"), float("inf"), True, last_move)
            last_move = make_move(board, best_move, 1)
            print(f"Player 1 calculates that the position is {score} points for him")
            print_board(board)
            if check_win(board, last_move):
                print(f"1 Won on round {i+1}")
                break

            if check_draw(board):
                print("Game drawn")
                break

            score, best_move = minimax(board, depth2, float("-inf"), float("inf"), False, last_move)
            last_move = make_move(board, best_move, 2)
            print(f"Player 2 calculates that the position is {score} points for him")
            print_board(board)
            if check_win(board, last_move):
                print(f"2 Won on round {i+1}")
                break
            if check_draw(board):
                print("Game drawn")
                break