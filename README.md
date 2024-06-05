# Hangman Game

Welcome to Hangman! This is a command-line version of the classic word-guessing game implemented in Python.

## Features

- **Single-player gameplay**: Enjoy hours of fun guessing words solo!
- **Word selection**: The game selects a random word from a predefined list.
- **Letter guessing**: Guess letters to uncover the hidden word.
- **Hint assistance**: Stuck on a word? Use the hint functionality to reveal a letter (at the cost of 3 guesses).
- **Score calculation**: Your score is calculated based on guess accuracy and word difficulty.

## Installation

1. **Clone the repository**: 
    ```bash
    git clone https://github.com/your-username/hangman-python.git
    ```
2. **Navigate to the project directory**:
    ```bash
    cd hangman-python
    ```
3. **Run the game**:
    ```bash
    python hangman.py
    ```

## Gameplay Instructions

- Guess letters to uncover the hidden word.
- You have 10 guesses to correctly guess the word.
- Incorrect guesses reduce the number of remaining guesses.
- If you need help, enter '!' to reveal a letter at the cost of 3 guesses.

## Additional Information

- The game selects a random word from a predefined list stored in `words.txt`.
- Modify `words.txt` to customize the word list for the game.
- The game keeps track of your score based on guess accuracy and word difficulty.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

