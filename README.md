## Hangman
A command-line hangman game written in Python. It uses the random module to pick a word from a list, and lets the player guess letters one at a time with six lives.

## Features
Random Word — Picks a random word from a list of 50 words each time a game starts.

Hidden Word Display — Shows the word as underscores and reveals correctly guessed letters in their positions.

Six Lives — Decreases a life for each wrong guess and ends the game when they run out.

Win Detection — Ends the game when every letter has been guessed.

Play Again — Restarts with a fresh word and reset lives if the user answers y.

Input Validation — Re-prompts if the user gives an invalid answer when asked to play again.

## Technologies Used
| Technology | Purpose |
|---|---|
| Python | Application logic |
| `random` | Picks a random word |
| List (`words`) | Stores the word pool |
| List (`guessed`) | Tracks revealed letters |
| `global` | Resets `lives`, `word`, and `guessed` between games |
| `input()` / `print()` | Console interaction |
| Recursion | Restarts the game via `play()` and `again()` |
<!-- -->
## How to Use It
Install Python 3.6 or newer from python.org and make sure it's added to your PATH.

Save the code as hangman.py.

Open a terminal in the folder containing the file.

Run python hangman.py.

Guess one letter at a time; you have 6 lives, and you can play again by answering y when prompted.

## Improvements
Validate letter guesses — the current code doesn't check that the input is a single letter, so entering a full word or number behaves unpredictably; check len(guess) == 1 and guess.isalpha() before processing.

Use a loop instead of recursion — play() and again() call each other every round, which stacks frames and will eventually hit Python's recursion limit; a while True loop is safer.
