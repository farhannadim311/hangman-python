import random
import string
import sys
# -----------------------------------
# HELPER CODE
# -----------------------------------
WORDLIST_FILENAME = "words.txt"
def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist
def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)
# -----------------------------------
# END OF HELPER CODE
# -----------------------------------
# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()
def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    secret_set = set(secret_word)
    guessed_set = set(letters_guessed)
    return secret_set.issubset(guessed_set)

def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    return ''.join([letter if letter in letters_guessed else '*' for letter in secret_word])
def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    all_letters = set(string.ascii_lowercase)
    letters_available = all_letters - set(letters_guessed)
    return ''.join(sorted(letters_available))        
def unique_letters(secret_word, availabe_letters):
    """Generates a unique letter when hint is called, takes in parameters the secret words
        and all the letters used"""
    choose_from = ''
    for i in availabe_letters:
        if i in secret_word:
            choose_from = choose_from + i
    new = random.randint(0, len(choose_from)-1) 
    revealed_letter = choose_from[new]
    return revealed_letter
def letters_in_secret_word(secret_word):
    """Returns all the unique letters in secret word, takes in only the secret word
    as the parameter"""
    unique = ''
    for i in secret_word:
        if i not in unique:
            unique = unique + i
    return len(unique)
def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
    length = len(secret_word)
    dash = "--------------"
    guess = 10
    x = ''
    hintx = ''
    print("Welcome to Hangman!")
    print(f"I am thinking of a word that is {length} characters long.")
    while (has_player_won(secret_word, x) == False):
        print(dash)
        print(f"You have {guess} guesses left.")
        print(f"Available letters: {get_available_letters(x)}")
        letters_guess = input("Please guess a letter: ")
        letters_guess.lower()
        while(letters_guess.isalpha() != True or len(letters_guess) > 1):
            if (with_help == True):
                if (letters_guess == '!'):
                    if (guess < 3):
                        print(f"Oops! Not enough guesses left: {get_word_progress(secret_word, x)}")
                        break
                    hintx = unique_letters(secret_word, get_available_letters(x))
                    x = x + hintx
                    print(f"Letter Revaled: {hintx}")
                    print(get_word_progress(secret_word, x))
                    guess -= 3
                    break      
            print(f"Oops! That is not a valid letter. Please input a letter from the aplhabet: {get_word_progress(secret_word,x)}")
            break
        if ((letters_guess in secret_word) and (letters_guess not in x) and (len(letters_guess) == 1) ):
            x = x + letters_guess
            print(f"Good Guess: {get_word_progress(secret_word , x)}")
        elif (letters_guess.isalpha() and len(letters_guess) == 1 and (letters_guess not in secret_word)):
            x = x + letters_guess
            print(f"Oops! That letter is not in my word: {get_word_progress(secret_word, x)}")
            if(letters_guess not in 'aeiou'):
                guess -= 1
            else:
                guess -= 2
        elif (letters_guess in x and letters_guess.isalpha() ):
            print(f"Oops! You have already guessed that letter: {get_word_progress(secret_word, x)}")
        if (has_player_won(secret_word, x)) == True:
            total_score = (guess + 4 * (letters_in_secret_word(secret_word)) + (3 * len(secret_word)))
            print(dash)
            print("Congratulations, you won!")
            print(f"Your total score for this game is: {total_score}")
            sys.exit()
        elif (guess < 1):
            print(dash)
            print(f"Sorry you ran out of guesses. The word was {secret_word}")
            sys.exit()
if __name__ == "__main__":
    secret_word = choose_word(wordlist)
    with_help = True
    hangman(secret_word, with_help)
    pass