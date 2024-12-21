import random

def choose_word():
    # List of words for the game
    word_list = ["python", "javascript", "hangman", "developer", "computer", "programming", "challenge","codeAlpha"]
    # Randomly choose a word from the list
    return random.choice(word_list)

def display_word(word, guessed_letters):
    # Display the word with underscores for unguessed letters
    return "".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6  # Number of attempts before losing
    guessed_word = False

    print("Welcome to the game Hangman!")
    print("Try guessing the word.")

    # Main game loop
    while attempts > 0 and not guessed_word:
        print("\nWord to guess: ", display_word(word, guessed_letters))
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print(f"Attempts left: {attempts}")

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue

        if guess in guessed_letters:
            print(f"You've already guessed the letter '{guess}'. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Great guess! The letter '{guess}' is in the word.")
        else:
            attempts -= 1
            print(f"Oops! The letter '{guess}' is not in the word.")

        # Check if the player has guessed all letters
        if all(letter in guessed_letters for letter in word):
            guessed_word = True

    if guessed_word:
        print(f"\nCongratulations! You've guessed the word '{word}' correctly.")
    else:
        print(f"\nGame over! The word was '{word}'.")
        print( "Better luck next Time.")

# Start the game
hangman()
