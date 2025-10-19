## Unit testing

### unit_test.py
#### test_make_move
Tests that after making a move to column 4 (index 3), the function `make_move` places the piece for the correct side at the correct position and returns the coordinates of the last move.

#### test_make_move_invalid_column_raises
Tests that when attempting to make a move outside the valid column range (0–6), the function `make_move` raises a `ValueError`.

#### test_make_move_full_column_raises
Tests that when trying to make a move into a column that is already full, the function `make_move` raises a `ValueError`.

#### test_check_win_horizontal
Tests that four consecutive moves in a horizontal line by the same player correctly trigger a win condition as detected by `check_win`.

#### test_check_win_vertical
Tests that four consecutive moves in a vertical line by the same player correctly trigger a win condition as detected by `check_win`.

#### test_check_draw_true_when_full
Tests that when the entire board is filled with alternating pieces and no winning pattern, the function `check_draw` correctly identifies the game as a draw.

#### test_heuristic_favors_center
Tests that the `heuristic` function assigns a higher value to positions where pieces are placed closer to the center column, confirming center-column preference.

#### test_heuristic_value
Tests that the `heuristic` function returns a **positive value** when the board favors player 1 and a **negative value** when the board favors player 2, ensuring correct sign conventions.

#### test_minimax_win_self
Tests that the `minimax` algorithm correctly identifies an immediate winning move for the current player within one turn.

#### test_minimax_win_opponent
Tests that the `minimax` algorithm correctly identifies a potential winning move for the opponent and blocks it within one turn.

#### test_minimax_return_when_depth_0
Tests that the `minimax` function stops search at depth 0 and returns a `(score, None)` tuple, indicating no further moves are considered.

#### test_minimax_return_when_draw
Tests that the `minimax` function correctly returns a draw evaluation `(0, None)` when the game board is full and no moves are available.

#### test_depth_calculation
Tests that the `minimax` algorithm can plan a win in three moves (within depth 5 search), correctly adjusting its move selection as the board state changes after each move sequence.

#### test_iterative_deepening_stops_in_time
Tests that the `iterative_deepening` function respects the specified time limit (0.5 seconds) and terminates within an acceptable margin (<2 seconds total execution), returning valid result and depth types.

#### test_iterative_deepening_detects_win_immediately
Tests that the `iterative_deepening` function detects an already-completed win condition instantly and returns `(None, None)` without unnecessary computation.

#### test_iterative_deepening_detects_win_in_one
Tests that the `iterative_deepening` function can recognize a guaranteed win-in-one move and returns a result tuple where the evaluation score equals the winning value (`100000`).

### Coverage
<img width="627" height="155" alt="image" src="https://github.com/user-attachments/assets/8e5bef36-5d34-438e-9f91-67ad26e049d3" />

Main.py is UI and I/O, which doesn't need to be tested.

## End-to-end testing

#### E2E_test.py
test_end_to_end runs a full simulated game between two AIs using iterative_deepening with random time limits within 0.1 seconds and 1 second. It ensures that both AIs always make valid moves and that the game terminates correctly within 42 moves (the full board).


## Integration testing
The integration testings can be done using command:
```
poetry run python main.py
```
After which user can test it by playing agaist it or watching two AI play.

More instructions on how to run the testings in [user instructions](https://github.com/Bladenoodle/C4-AI/blob/main/Documentations/User%20Instructions.md).
