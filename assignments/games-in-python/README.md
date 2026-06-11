
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build the classic word-guessing game where players guess letters to reveal a hidden word before running out of attempts. You'll practice string manipulation, loops, conditionals, and random selection.

## 📝 Tasks

### 🛠️ Create the Core Game Logic

#### Description
Set up the game structure with a word list, game state tracking, and the main game loop that handles user input and updates the game progress.

#### Requirements
Completed program should:

- Randomly select words from a predefined list
- Accept letter guesses from the player
- Display current progress in underscore format (_ _ _)
- Track incorrect guesses remaining
- Continue until the word is guessed or attempts are exhausted

### 🛠️ Implement Win/Lose Messages and Game Flow

#### Description
Add end-game detection and display appropriate messages when the player wins or loses. Provide an option to play again.

#### Requirements
Completed program should:

- Display a win message when the word is correctly guessed
- Display a lose message when attempts are exhausted (showing the correct word)
- Offer the player a choice to play another round
- Handle invalid input gracefully (duplicate guesses, non-alphabetic characters)
