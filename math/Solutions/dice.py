import random

def roll_die(sides=6):
    num_rolled = random.randint(1, sides)
    return num_rolled

def main():
    sides = 6
    total = 0

    num_rolls = 1
    roll = roll_die(sides)
    print("You rolled a", roll)
    total += roll
    print("Total after first roll:", total)

    num_rolls += 1
    roll = roll_die(sides)
    print("You rolled a", roll)
    total += roll
    print("Total after", num_rolls, "rolls:", total)

    num_rolls += 1
    roll = roll_die(sides)
    print("You rolled a", roll)
    total += roll
    print("Total after", num_rolls, "rolls:", total)

    average = round(total / num_rolls, 2)
    print("Your average roll was", average)

    print("Thanks for playing.")

main()