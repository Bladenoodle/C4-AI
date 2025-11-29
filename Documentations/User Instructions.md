# User Instructions

## Overview
This program implements a connect 4 game where you can either **play against a minimax AI** or **watch two AIs play against each other**.  
The AI uses *iterative deepening*, *alpha–beta pruning*, and *move ordering* for efficient decision-making.

---
## Installation

This project uses **Poetry** for dependency management.  
Make sure you have **Poetry ≥ 1.2** installed (older versions do not support the modern `[project]` table format in `pyproject.toml`).

### 1. Install Poetry
If you don’t have Poetry yet, install it with:

```
curl -sSL https://install.python-poetry.org | python3 -
```
Then verify your version to be ≥ 1.2 with:
```
poetry --version
```
If the version is too old, you can update with:
```
poetry self update
```

Lastly install Poetry dependencies with:
```
poetry install
```

## How to Run the Program

**Choose what to do**

Now you can either:
- **Play the game** (main program)
- **Run tests** to verify functionalities

---

## Play
Start the game with:
```
poetry run python main.py
```

After launch, you will see:
```
Welcome to Connect 4
Play against bot (play)
Watch bots play (watch)
Choose a mode (play/watch/exit):
```
### 1. Playing Against the AI
When you choose `play`, you will be asked:
```
Play first? (y/n):
```
- `y` → You play as Player 1
- `n` → You play as Player 2

Next, choose how long the AI should calculate its move:
```
Choose enemy calculation time:
```
Enter a **number of seconds**, for example:
```
2
```
The AI will then think for up to 2 seconds per move.

Now the game begins. When it’s your turn, make a move by typing the **column number (1–7)** where you want to drop your piece:
```
Make a move: 4
```

The board is displayed after every move.  
The program automatically announces when a player wins or when the game ends in a draw.

---

### 2. Watch Mode (AI vs AI)
You can also let two minimax AIs play against each other.

Select:
```
watch
```

Then, you’ll be prompted to choose each AI's calcuation time:
```
Choose player 1 calculation time:
Choose player 2 calculation time:
```

The two AIs will then play automatically until one wins or the game is drawn.  
The terminal displays their evaluations and chosen moves after each turn.

---

### Exit
To quit the program, type:
```
exit
```
and press Enter.

### Notes
- **Calculation time** determines how deep the AI calculates.
  Longer times allow deeper and usually smarter decisions.
  **Too large times will make you wait longer!** (if stuck, press ctrl + C)
- The AI prints messages describing its thought process, for example:
```
calculation time: 1.76 seconds
Player 1 calculates with a depth of 10 that the position is -4 points for him
```

- The game ends automatically when:
- Either player connects four pieces in a row, or  
- The board is full (draw).

## Testing
The program has three different testing options.
### Unit testing
For simple unit testing:
```
Poetry run invoke test
```
### Unit testing with coverage:
```
Poetry run invoke coverage
```
### End-to-end testing
```
Poetry run invoke E2E
```


More details about testing in [testing document](https://github.com/Bladenoodle/C4-AI/blob/main/Documentations/Testing%20Ducoment.md).
