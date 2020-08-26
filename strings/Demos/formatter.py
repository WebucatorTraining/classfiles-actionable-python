import math

def main():
    again = ''
    while again != "q":
        f = input("Format to try: ")
        try:
            n = eval(input("Entry to format: "))
            print("Result: ", f.format(n))
        except:
            print('Invalid entries.')
            raise
        again = input("Enter for another or 'q' to quit. ")

main()