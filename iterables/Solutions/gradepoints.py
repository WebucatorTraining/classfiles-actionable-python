def main():
    grades = {}
    grades["English"] = int(input("English grade: "))
    grades["Math"] = int(input("Math grade: "))
    grades["Global Studies"] = int(input("Global Studies grade: "))
    grades["Art"] = int(input("Art grade: "))
    grades["Music"] = int(input("Music grade: "))

    gradepoints = grades.values()

    average = sum(gradepoints)/len(gradepoints)

    print("Your average is", average)

main()