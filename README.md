🎮 Python Hangman Game
A simple command-line Hangman game built with Python. Players try to guess a hidden word one letter at a time before running out of lives. It's a great beginner project for learning about lists, loops, functions, global variables, and random selection in Python.

📖 Python Hangman Game
The Python Hangman Game is a console-based word-guessing game. A random word is selected from a built-in list of 50 words, and the player must guess it letter by letter.

The player starts with 6 lives. Each correct guess reveals all matching letters in the word, while each wrong guess costs a life. The game ends when the player either reveals the entire word (win) or runs out of lives (lose). After each game, the player is asked whether they'd like to play again.

This project is ideal for anyone learning the fundamentals of Python — especially loops, conditionals, functions, and list manipulation.

✨ Features
50-word built-in word list – A wide variety of words including lantern, whisper, glacier, monsoon, and more.

Random word selection – A new word is chosen each game using random.choice().

6 lives per game – Lose a life for each incorrect guess.

Letter-by-letter guessing – Reveals all occurrences of a correct letter.

Live word display – Shows the current progress as underscores and revealed letters.

Win detection – Automatically detects when the full word is guessed.

Lose detection – Reveals the correct word when lives reach zero.

Replay option – Play again without restarting the program.

Input validation – Prompts the user again if an invalid response is given to the replay question.

Word length hint – Displays how many letters the hidden word has.

🛠️ What It Uses
Language & Library
Python 3

random – Python's built-in module for random word selection.

Key Variables
Variable	Purpose
lives	Number of remaining guesses (starts at 6).
words	A list of 50 possible words to guess.
word	The randomly selected word for the current game.
guessed	A list of underscores and revealed letters representing the player's progress.
Key Functions
Function	Purpose
play()	Runs a full game of Hangman, resetting lives, word, and guessed letters.
again()	Asks the player whether they'd like to play again and handles the response.
Python Concepts Demonstrated
The random module – Using random.choice() to pick a word.

Lists – Storing words and tracking guessed letters.

List multiplication – ["_"] * len(word) to create the initial display.

global keyword – Modifying global variables inside functions.

while loops – The main game loop.

for loops – Iterating through letters in the word.

Conditional logic – Checking correct/incorrect guesses and win/lose states.

Functions – Organizing the game into reusable blocks.

Recursion – again() calls itself if an invalid response is given, and play() calls again() at the end.

String methods – .lower() and .strip() for clean input.

join() – Displaying the guessed word in a readable format.

Built-in Functions Used
input() – Reads user input from the console.

print() – Displays prompts, game state, and results.

random.choice() – Picks a random word from the list.

len() – Gets the length of the word.

range() – Iterates through the word's positions.

str() – Converts the lives count to a string for display.

exit() – Ends the program cleanly.

📥 Download
You can download the source file from this repository and save it as a .py file:

text
hangman.py
No installation or dependencies are needed — just Python.

▶️ How to Run
Make sure you have Python 3 installed (python.org).

Save the code as hangman.py.

Open a terminal or command prompt in the folder containing the file.

Run:

bash
python hangman.py
Start guessing letters and try to reveal the hidden word before you run out of lives!

🐍 Made with Python
This project is written entirely in Python 3 using only the standard library. It's a fun and classic example of how loops, lists, and randomization can be combined to build a small game.

Whether you're a beginner practicing control flow or someone who just enjoys word games, this project is a great starting point.

💡 Possible Future Improvements
Add ASCII art for the hangman drawing that updates with each wrong guess.

Prevent duplicate guesses – Warn the player if they've already guessed a letter.

Validate input – Ensure only single alphabetic characters are accepted.

Add difficulty levels – Fewer lives for harder modes, or longer words.

Categorize words – Let players choose a theme (animals, food, etc.).

Track wins and losses – Display stats across multiple games.

Save and load words from an external file.

Build a Tkinter GUI version for a graphical interface.

📄 License
This project is free to use, modify, and distribute for personal or educational purposes.
