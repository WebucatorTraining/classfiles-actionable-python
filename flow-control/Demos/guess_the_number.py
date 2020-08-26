import random

def is_valid_num(s):
    # Make sure the number is a digit between 1 and 100.
    return s.isdigit() and 1 <= int(s) <= 100

def main():
    # Get a random number between 1 and 100
    number = random.randint(1, 100)

    # Set guessed_number to False to start.
    # We'll set it to True when the user guesses the number
    guessed_number = False

    # Get the user's guess
    guess = input("Guess a number between 1 and 100: ")

    # Set num_guesses to 0.
    # We'll increment it by 1 after each guess
    num_guesses = 0

    # We'll keep looping until the user guesses the number
    while not guessed_number:
        # Make sure the number is valid
        if not is_valid_num(guess):
            print("I won't count that one.")
            guess = input("A number between 1 and 100 please: ")
        else: # Number is valid
            num_guesses += 1 # Increment num_guesses
            guess = int(guess) # Convert user's guess to an int

            # If guess is wrong, provide info and ask for another guess
            if guess < number:
                guess = input("Too low. Guess again: ")
            elif guess > number:
                guess = input("Too high. Guess again: ")
            else:
                print("You got it in", num_guesses, "guesses!")
                guessed_number = True # This will break us out of loop

    print("Thanks for playing.")

main()