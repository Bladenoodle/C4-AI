"""Main program for playing and testing Connect 4 minimax with iterative deepening."""

import time
from connect_4 import(
    make_move, print_board, check_win, minimax,
    create_board, check_draw
)

def iterative_deepening(board, cal_time, maximizing, last_move):
    """
    Function for calling minimax in a deepening search.
    Minimax runs iteratively depth by depth until the given calculation time is reached.
    """
    start_time = time.time()
    if check_win(board, last_move):
        return (None, None), None
    memory = {}
    depth = 0
    best_eval, best_move = 0, None
    while time.time() - start_time < cal_time:
        depth += 1
        best_eval, best_move = minimax(
            board, depth, float("-inf"), float("inf"),
            maximizing, memory, last_move
        )
        if abs(best_eval) >= 100000:
            break
    return (best_eval, best_move), depth


def play_game(side, cal_time):
    """
    Function for playing against the minimax algorithm.
    Assigns player to the side they desired.
    The opponent is a minimax that calculates a fixed time.
    """
    board = create_board()
    last_move = None
    for i in range(22):
        if side == 1:
            best_move = int(input("Make a move: ")) - 1
            last_move = make_move(board, best_move, 1)
            print_board(board)
            if check_win(board, last_move):
                print(f"1 Won on round {i+1}")
                break
            if check_draw(board):
                print("Game drawn")
                break

            best, cal_depth = iterative_deepening(board, cal_time, False, last_move)
            best_eval, best_move = best
            last_move = make_move(board, best_move, 2)
            print(f"Player 2 calculates with a depth of {cal_depth} "
                  f"that the position is {-best_eval} points for him")
            print_board(board)
            if check_win(board, last_move):
                print(f"2 Won on round {i+1}")
                break
            if check_draw(board):
                print("Game drawn")
                break
        else:
            best, cal_depth = iterative_deepening(board, cal_time, True, last_move)
            best_eval, best_move = best
            last_move = make_move(board, best_move, 1)
            print(f"Player 1 calculates with a depth of {cal_depth} "
                  f"that the position is {best_eval} points for him")
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


def main():
    """
    The main program of testing minimax in terminal environment.
    The player has two choices:
    1. Play against the bot -> choose side and calculation depth for minimax.
    2. Watch two minimax play -> choose the starting position and their calculation depth.
    """
    choice = None
    print("Welcome to Connect 4")
    while choice != "exit":
        print("Play against bot (play)")
        print("Watch bots play (watch)")
        choice = input("Choose a mode (play/watch/exit): ").strip().lower()

        while choice == "play":
            first = input("Play first? (y/n): ").strip().lower()
            cal_time = int(input("Choose enemy calculation time: "))
            if first == "y":
                play_game(1, cal_time)
                choice = None
                time.sleep(1)
            if first == "n":
                play_game(2, cal_time)
                choice = None
                time.sleep(1)

        while choice == "watch":
            board = create_board()
            cal_time1 = int(input("Choose player 1 calculation time: "))
            cal_time2 = int(input("Choose player 2 calculation time: "))
            last_move = None

            for i in range(22):
                best, cal_depth = iterative_deepening(board, cal_time1, True, last_move)
                best_eval, best_move = best
                last_move = make_move(board, best_move, 1)
                print(f"Player 1 calculates with a depth of {cal_depth} "
                      f"that the position is {best_eval} points for him")
                print_board(board)
                if check_win(board, last_move):
                    print(f"1 Won on round {i+1}")
                    choice = None
                    break

                if check_draw(board):
                    print("Game drawn")
                    choice = None
                    break

                best, cal_depth = iterative_deepening(board, cal_time2, False, last_move)
                best_eval, best_move = best
                last_move = make_move(board, best_move, 2)
                print(f"Player 2 calculates with a depth of {cal_depth} "
                      f"that the position is {-best_eval} points for him")
                print_board(board)
                if check_win(board, last_move):
                    print(f"2 Won on round {i+1}")
                    choice = None
                    break
                if check_draw(board):
                    print("Game drawn")
                    choice = None
                    break


if __name__ == "__main__":
    main()
