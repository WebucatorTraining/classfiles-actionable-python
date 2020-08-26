def main():
    phrase = input("Choose a phrase: ")
    print("Your phrase is '", phrase, "'", sep="")
    pos = int(input("Which character? [Enter number] "))-1
    print("Character ", pos+1, " is '", phrase[pos], "'", sep="")

main()