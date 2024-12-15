while True:
    guess = input("Please guess a letter: ")
    if len(guess) == 1 and guess.isalpha():
        print("Good guess!")
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")
