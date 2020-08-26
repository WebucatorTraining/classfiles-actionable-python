def divide(num, den):
    remainder = num % den
    floor = num // den
    print(num, "divided by", den, "equals",
          floor, "with a remainder of", remainder)

def main():
    divide(5, 2)
    divide(6, 3)
    divide(12, 5)
    divide(1, 2)

main()