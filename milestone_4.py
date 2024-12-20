import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.word = random.choice(word_list)  
        self.word_guessed = ['_' for _ in self.word] 
        self.num_letters = len(set(self.word))  
        self.num_lives = num_lives  
        self.list_of_guesses = []  
    def check_guess(self, guess):
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
            print(f"You have {self.num_lives} lives remaining.")
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
if __name__ == "__main__":
    word_list = ["apple", "banana", "cherry", "mango", "orange"]
    hangman_game = Hangman(word_list)
    while hangman_game.num_lives > 0 and hangman_game.num_letters > 0:
        print(f"Word to guess: {' '.join(hangman_game.word_guessed)}")
        hangman_game.ask_for_input()
    
    if hangman_game.num_letters == 0:
        print(f"Congratulations! You guessed the word: {''.join(hangman_game.word)}")
    else:
        print(f"Game over! The word was: {''.join(hangman_game.word)}")
