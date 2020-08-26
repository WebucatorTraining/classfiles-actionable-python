def main():
    dice_rolls = [
        (a, b)
        for a in range(1, 7)
        for b in range(1, 7)
    ]

    print(dice_rolls)

main()