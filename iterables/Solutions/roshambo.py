import random

def main():
    roshambo = ["Rock", "Paper", "Scissors"]

    computer_choice = random.choice(roshambo)

    num = input("1 for Rock, 2 for Paper, 3 for Scissors: ")
    num = int(num) - 1
    user_choice = roshambo[num]

    print("Computer:", computer_choice)
    print("User:", user_choice)

main()