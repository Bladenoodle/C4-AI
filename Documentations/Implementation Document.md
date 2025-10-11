## Program structure
connect_4.py contains the basic functions for a connect four game, different kinds of win and draw checking, a heuristic function, and a minimax algorithm with alpha-beta pruning.

main.py contains the function for iterative deepening, a function for a match between a human and AI, and the main program for testing the AI by either playing a game against it or watching it play against itself.

Tests will be explained in the [Testing Document](https://github.com/Bladenoodle/C4-AI/blob/main/Documentations/Testing%20Ducoment.md).

## Time compexity
Time complexity with alpha-beta pruning is around O(b^(d/2)), where b is the average number of available moves and d is the chosen depth of calculation. The b is practically 7 most of the time, making the time compexity approximately O(7^(d/2)). Calculating the moves starting from the middle is theoretically a big optimization in time complexity for a connect 4 AI, because the optimal move is close to the center in most of the time, and with alpha-beta pruning away the worse choices, this will greatly improve the performace. However, I couldn't find any sources for this, so I can only say for sure that the time complexity is <O(b^(d/2)).

## Space complexity
Space complexity is O(b^(d/2)), because we can concieve the execution of minimax to search 1 branch to the depth d at a time and deletes it afterwards, making it O(d). We also added a transposition table called 'memory', which stores all the positions calculated this run, which makes the memory to hold up to the same amount of position as calculated, which is O(b^(d/2)) based on time complexity. Now adding them up we get O(d+b^(d/2)). The rule of big O notation states that this is equal to O(b^(d/2)).

## Performance & Complexity comparison
In the starting position, the AI takes 1.67 seconds to calculate 10 moves, and 4.85 seconds to calculate 11 moves. Calculating the quotient, we get that the time increases roughly 2,9 times every depth, which is very close to 7^(1/2) ≈ 2.65. The difference may be caused by little inefficiencies in the code that adds up, but we can safely say that the program is performing at the time complexity of O(b^(d/2)).

## Possible improvements
- Heuristic function optization
- More efficient programming language than python such as C++

## AI usage
The help of LLM has only been used in debugging, information gathering, helping with pylint and github operations, polishing existing program, and as a "rubber duck" (see rubber duck debugging).

## Sources
- Connect 4 solver: https://connect4.gamesolver.org/
- Connect 4 puzzles: https://sites.math.rutgers.edu/~zeilberg/C4/C4.html
- Minimax -- Wikipedia: https://en.wikipedia.org/wiki/Minimax Accessed: 11.10.2025
- Minimax complexities: https://stackoverflow.com/questions/2080050/how-do-we-determine-the-time-and-space-complexity-of-minmax Accessed: 11.10.2025
  

