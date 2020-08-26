with open("../data/1880-boys.txt") as f_boys:
    boys = f_boys.read()

with open("../data/1880-girls.txt") as f_girls:
    girls = f_girls.read()

with open("../data/1880-all.txt", "w") as f:
    f.write(boys + "\n" + girls)