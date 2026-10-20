Hangman
A command-line Python Hangman game where the player guesses letters to reveal a random word before running out of lives.

Concepts Used
Lists — guessed starts as underscores and is updated as letters are found.

Random Module — random.choice(words) picks a random word from a 50-word list.

Global Variables — lives, word, and guessed are modified inside play() via global.

Features
Random Word Selection — a new word is chosen each round from a large word list.

Six Lives — wrong guesses reduce lives; the word is revealed on a loss.

Win/Loss Detection — checks for a fully revealed word to trigger a win.

Improvements
Track Repeated Guesses — guessing the same letter twice currently costs a life or re-counts; store past guesses and warn instead.

Validate Input — single-letter check needed; empty or multi-letter input breaks the logic.

Replace Recursion & Globals — again() calls play() recursively; a loop plus passing state as arguments is cleaner and avoids deep call stacks.

