Test 1:
The first test with the progress of week 3, that is having alpha beta pruning.
The algorithm is interestingly inefficient. When it calculates a win, it doesn't go for the shortest path to the win. It will secure a win when its the only move, but when thats not the case it might take a long path to victory. I believe this is because in its program, if it has many moves that are equally good, it's programmed to choose the first discovered one. Win in 5 or win in 1 is equally good in its "eyes", so it is up to luck, which one it sees first. This will be fixed by next week.

Conclution: The algorithm finds solutions up to win in 4, but it doesn't prioritize the shortest path to winning.

Week 3 testing:
10 Testing with different puzzles, and it can solve every win in 4, can't solve any win in 5.

The criterion to did it find a solution or not is by printing out its evaluation of the position. If the position is "inf", it has already solved it. Puzzles used for testing is from:
https://sites.math.rutgers.edu/~zeilberg/C4/ch4/P10.html

Example of win in 4 puzzle:
Puzzle (Chapter IV -- problem 10):
   1   2   3   4   5   6   7 
 +---+---+---+---+---+---+---+
 |   |   |   |   |   |   |   |
 +---+---+---+---+---+---+---+
 |   |   |   |   |   |   |   |
 +---+---+---+---+---+---+---+
 |   |   | X |   |   | X | X |
 +---+---+---+---+---+---+---+
 | O |   | X |   | X | O | O |
 +---+---+---+---+---+---+---+
 | O |   | O |   | X | O | O |
 +---+---+---+---+---+---+---+
 | X |   | O |   | O | X | X |
 +---+---+---+---+---+---+---+
Code:
##############################################
from connect_4 import ConnectFour
from main import minimax

win_in_two = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 1],
    [2, 0, 1, 0, 1, 2, 2],
    [2, 0, 2, 0, 1, 2, 2],
    [1, 0, 2, 0, 2, 1, 1],
]

game = ConnectFour(board=win_in_two)

for i in range(25):
    game.make_move(minimax(game, 7, True))
    game.print_board()
    if game.check_win(1):
        print(f"1 Won on round {i}")
        break

    game.make_move(minimax(game, 6, False))
    game.print_board()
    if game.check_win(2):
        print(f"2 Won on round {i}")
        break
##############################################

Output (inf:
##############################################

Evaluation: inf

   1   2   3   4   5   6   7 
 +---+---+---+---+---+---+---+
 |   |   |   |   |   |   |   |
 +---+---+---+---+---+---+---+
 |   |   |   |   |   |   | X |
 +---+---+---+---+---+---+---+
 |   |   | X |   |   | X | X |
 +---+---+---+---+---+---+---+
 | O |   | X |   | X | O | O |
 +---+---+---+---+---+---+---+
 | O |   | O |   | X | O | O |
 +---+---+---+---+---+---+---+
 | X |   | O |   | O | X | X |
 +---+---+---+---+---+---+---+

##############################################

