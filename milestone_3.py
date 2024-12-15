
import random

# Create a list of words for the game
def create_word_list():
    """Create and return a list of words for the Hangman game."""
    return ["apple", "banana", "cherry", "mango", "orange"]

# Choose a random word from the word list
def choose_random_word(word_list):
    """Choose and return a random word from the given word list."""
    return random.choice(word_list)

# Validate user input
def is_valid_input(input_str):
    """
    Validate the user input.
    Input must be a single alphabetical character.
    """
    return len(input_str) == 1 and input_str.isalpha()

# Check if the guessed letter is in the secret word
def check_guess(secret_word, guess):
    """
    Check if the guessed letter is in the secret word.
    Prints appropriate messages based on the guess.
    """
    guess = guess.lower()
    if guess in secret_word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

# Ask the user for input
def ask_for_input(secret_word):
    """
    Continuously ask the user for a valid letter guess
    and check if it is in the secret word.
    """
    while True:
        guess = input("Please guess a letter: ")

        # Validate the input
        if is_valid_input(guess):
            # Check the guess and exit the loop
            check_guess(secret_word, guess)
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

# Main game logic
def main():
    """
    Main function to run the Hangman game.
    """
    # Step 1: Create a list of words and choose a random word
    word_list = create_word_list()
    secret_word = choose_random_word(word_list)

    # Step 2: Start the input and guessing process
    ask_for_input(secret_word)

# Run the game
if __name__ == "__main__":
    main()
