import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        """
        Initialize the Hangman class with the following attributes:
        
        :param word_list: list of words from which a random word will be chosen
        :param num_lives: number of lives the player starts with (default is 5)
        """
        self.word_list = word_list
        self.word = random.choice(word_list)  # Randomly pick a word from the word_list
        self.word_guessed = ['_' for _ in self.word]  # List representation of the word, initially hidden
        self.num_letters = len(set(self.word))  # Unique letters in the word to be guessed
        self.num_lives = num_lives  # Number of lives the player starts with
        self.list_of_guesses = []  # List to track letters guessed by the player

    def check_guess(self, guess):
        """
        Check if the guessed letter is in the word.
        
        :param guess: The letter guessed by the user
        """
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess
            self.num_letters -= 1
        else:
            print(f"Sorry, {guess} is not in the word.")
            self.num_lives -= 1

    def ask_for_input(self):
        """
        Continuously ask the user to guess a letter and validate the input.
        """
        while True:
            guess = input("Guess a letter: ")
            if not guess.isalpha() or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

# Example usage:
if __name__ == "__main__":
    word_list = ["apple", "banana", "cherry", "mango", "orange"]
    hangman_game = Hangman(word_list)
    hangman_game.ask_for_input()
