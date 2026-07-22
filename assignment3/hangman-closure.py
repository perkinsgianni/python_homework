# Task 4: Closure Practice

def make_hangman(secret_word):
    # initialize empty list for guesses
    guesses = []

    # accept letter
    def hangman_closure(letter):
        # append letter to guesses list
        guesses.append(letter)

        # substitute "_" for letters not guessed, join char
        guessed_word = "".join([char if char in guesses else "_" for char in secret_word])
        print(f"Guessed word: {guessed_word}")

        # return true if all letters guessed; otherwise, return false
        return "_" not in guessed_word

    return hangman_closure

# establish secret word
secret_word_input = input("Enter secret word: ")
# print(f"Secret word: {secret_word_input}")

# initialize closure with secret word
play_make_hangman = make_hangman(secret_word_input)
# print(f"Function obj: {play_make_hangman}")

while True:
    # prompt user for single letter guess
    guess = input("Make a guess: ")
    
    # check if all letters have been guessed
    all_letters_guessed = play_make_hangman(guess)
    # print(f"All letters guessed? {all_letters_guessed}")
    
    # exit loop if closure returns true
    if all_letters_guessed:
        print("Congratulations, you guessed the secret word!")
        break