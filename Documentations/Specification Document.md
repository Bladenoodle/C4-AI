This project is about making an AI that plays Connect 4.

The developer of the project knows only python, so the program will be purely made with python and developer can only peer-review other python projects.

The goal of the project is to implement minimax algorithm and alpha beta pruning to make the AI able to count as many moves ahead as possible.

The program is expected to get an input with a two-dimentional list and the and a integer value 0 or 1. The list will be in size 6x7, which is the size of a Connect 4 game and it will contain the position that needs to be analyzed. The integer value is to define which side is the AI analyzing for. 

Minimax algorithm optimized with alpha beta pruning is an effective way of building an AI to play a 1v1 turn-based game. 

Minimax algorithm recursively goes down paths in depth order forming a tree indicating the heuristic values of possible choices. For example if depth is 2 and the position is starting position, where the board is empty, the recursion works as follows: (Depth 0) The algorithm goes through all the possible moves it can make, which is 6 in this position, and make a new node per move. (Depth 1) With new nodes we also calculate all the possible responses, which refers to all the opponent's possible moves and make a new node per move. (Depth 2) The algorithm uses a function(not yet done) to decide a heuristic value for each node, which indicates how good the position is for "us". The algorithm goes up in depth (Depth 1) and choses to make the move or one of the moves with the minimum heuristic value(optimal for the opponent), after which the nodes in this depth gets the minimum heuristic value of its children. Finally, the algorithm goes one up in depth (Depth 0) and chooses one of the children with the highest heuristic value and plays the move. In summary, the algorithm calculates the best respose, if the opponent reacts optimally with the same way to value the position.

Alpha beta pruning is yet unclear how it works for me. I will return to this part after learning more about it!

The theoretical time complexity for alpha beta pruned algorithm is O(b^(d/2). The b is the average amount of possible moves in any game state, which I estimate to be very close to 7, which is the numbers of columns there are in the game. The d is the depth it calculates.

The purpose  of the course is for me to learn how to make a proper AI using minimax algoriyhm and alpha beta pruning and possibly other algorithms I need to learn along the way. **My question at the moment of writing this SD is what factors determine the effectiveness of the program. I will update on this when I think I have an answer!**

Programme: TKT

Sources:
- https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
- https://indiaai.gov.in/article/understanding-the-minmax-algorithm-in-ai
- https://stackoverflow.com/questions/16328690/how-do-you-derive-the-time-complexity-of-alpha-beta-pruning
