# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build the classic word-guessing game using Python strings, loops, and user input. You will create a Hangman game where players guess letters to reveal a hidden word before running out of attempts.

## 📝 Tasks

### 🛠️ Implement Word Selection

#### Description
Create a system to randomly select a word from a predefined list that the player will need to guess.

#### Requirements
Completed program should:

- Have a predefined list of words to choose from
- Randomly select one word from the list at the start of each game
- Keep the selected word hidden from the player


### 🛠️ Build the Guessing System

#### Description
Implement the core game logic that allows players to guess letters and displays their progress.

#### Requirements
Completed program should:

- Accept letter guesses from the player
- Display current progress in "_ _ _" format showing correctly guessed letters
- Track and display the number of incorrect guesses remaining
- Validate user input (single letters only)


### 🛠️ Add Game End Conditions

#### Description
Create win and lose conditions with appropriate feedback messages for the player.

#### Requirements
Completed program should:

- End the game when the word is completely guessed (win condition)
- End the game when attempts are exhausted (lose condition)
- Display appropriate win or lose messages
- Reveal the correct word when the game ends