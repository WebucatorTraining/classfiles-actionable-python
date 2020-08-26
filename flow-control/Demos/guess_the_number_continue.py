import random

def is_valid_num(s):
    return s.isdigit() and 1 <= int(s) <= 100

def main():
    number = random.randint(1, 100)
    guessed_number = False
    guess = input("Guess a number between 1 and 100: ")
    num_guesses = 0

    while not guessed_number:
        if not is_valid_num(guess):
            print("I won't count that one.")
            guess = input("A number between 1 and 100 please: ")
            continue # Skip to next iteration through loop

        num_guesses += 1
        guess = int(guess)

        if guess < number:
            guess = input("Too low. Guess again: ")
        elif guess > number:
            guess = input("Too high. Guess again: ")
        else:
            print("You got it in", num_guesses, "guesses!")
            guessed_number = True

    print("Thanks for playing.")

main()