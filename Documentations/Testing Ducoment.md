## Unit testing

### test_c4.py
- test_make_move tests that after making a move to col 4, the function make_move makes the correct move for the correct side and returns the correct last move.

- test_make_move_invalid_column_raises tests that when trying to make a move that is outside of the board, the function make_move raises a value error.

- test_make_move_full_column_raises tests that when trying to make a move to a full column, the function make_move raises a value error.

- test_check_win_horizontal tests that four consecutive moves horizontally by the same side correctly trigger a win condition.

- test_check_win_vertical tests that four consecutive moves vertically by the same side correctly trigger a win condition.

- test_check_draw_true_when_full tests that when all cells are filled, the function check_draw correctly identifies a draw.

- test_heuristic_favors_center tests that the heuristic function gives a higher value for center columns, ensuring positional preference.

- test_heuristic_value tests that heuristic values are positive when player 1 is favored and negative when player 2 is favored.

- test_minimax_win_self tests that the minimax algorithm can correctly detect a winning move for itself within one turn.

- test_minimax_win_opponent tests that the minimax algorithm can correctly detect a winning move for the opponent within one turn.

- test_minimax_return_when_depth_0 tests that the minimax function correctly returns a None move when the search depth is zero.

### test_main.py
- test_iterative_deepening_stops_in_time tests that the iterative_deepening function respects the given time limit and completes in under one second for a 0.5 second limit.

- test_iterative_deepening_detects_win_immediately tests that iterative_deepening exits immediately when the game has already been won before search begins.

### Coverage
<img width="623" height="185" alt="image" src="https://github.com/user-attachments/assets/446dff22-b111-4f40-acf1-2a393f078f45" />

The lines 19-56 and 60-64 that weren't tested in connect_4.py are UI functionalities.
The the lines that weren't tested in main.py are all I/O functionalities.

## Advanced testing
### test_E2E.py
test_end_to_end runs a full simulated game between two AIs using iterative_deepening with random time limits within 0.1 seconds and 1 second. It ensures that both AIs always make valid moves and that the game terminates correctly within 42 moves (the full board).

### test_puzzles.py
test_depth_calculation tests that minimax correctly identifies a forced win in 5 moves (depth 9) for a set of predefined puzzle states. It verifies that minimax returns the expected maximum heuristic value of 100,000, confirming correct depth calculation and win detection.

## Manual testing
The manual testings using command python src/main.py and playing against the AI myself, with itself and with a perfect connect 4 solver, I found that the AI is consistantly winning me, inconsistantly winning itself depending on depth, and almost always losing to a perfect solver, even in a theretical win state (starts first). This is most likely due to a poor heuristic function.
