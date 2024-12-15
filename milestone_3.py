
import random

# Create a list of words for the game
word_list = ["apple", "banana", "cherry", "mango", "orange"]

# Randomly choose a word from the list
secret_word = random.choice(word_list)

# Step 1: Define the check_guess function
def check_guess(guess):
    # Step 2: Convert the guess to lowercase
    guess = guess.lower()
    # Step 3: Check if the guess is in the word
    if guess in secret_word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

# Step 1: Define the ask_for_input function
def ask_for_input():
    while True:
        # Step 2: Ask the user to guess a letter
        guess = input("Please guess a letter: ")

        # Validate the guess
        if len(guess) == 1 and guess.isalpha():
            # Step 3: Call check_guess to check if the guess is in the word
            check_guess(guess)
            break  # Exit the loop after a valid guess
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

# Step 4: Call the ask_for_input function to test your code
ask_for_input()
