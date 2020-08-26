def main():
    phrase = input("Choose a phrase: ")
    print("Your phrase is '", phrase, "'", sep="")
    pos1 = int(input("Character to start with? [Enter number] "))
    pos2 = int(input("Character to end with? [Enter number] ")) + 1
    print("Your substring is '", phrase[pos1:pos2], "'", sep="")

main()