import random
fruit_choices = [ "mangos", "watermelons", "apples", "grapes", "bananas"]
fruit_list = fruit_choices
print(fruit_list)
word = random.choice(fruit_list)
print(word)
letter_guess = input("Enter a single letter: ")
if len(letter_guess) == 1 and letter_guess.isalpha():
  print("Good guess!")
else:
  print("Oops! That is not a valid input:")
#Comment

