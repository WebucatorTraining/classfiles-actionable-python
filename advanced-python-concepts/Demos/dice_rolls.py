def main():
    dice_rolls = []
    for a in range(1, 7):
        for b in range(1, 7):
            roll = (a, b)
            dice_rolls.append(roll)

    print(dice_rolls)

main()