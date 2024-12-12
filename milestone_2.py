import random
favorite_fruits = [ "mangos", "watermelons", "apples", "grapes", "bananas"]
word_list = favorite_fruits
print(word_list)
word = random.choice(word_list)
print(word)
guess = input("Enter a single letter: ")
print("Your guess is:", guess)
