import csv

csvfile = '../data/population-by-state.csv'
with open(csvfile, newline='', encoding="utf-8") as csvfile:
    pops = csv.DictReader(csvfile)
    print('Headers:', pops.fieldnames)
    for row in pops:
        # Convert to integers
        pop_2020 = int(row['2020'].replace(',', ''))
        pop_2010 = int(row['2010'].replace(',', ''))

        growth = pop_2020 - pop_2010

        # Use "," format spec to separate 1000s with commas 
        print(f"{row['State']}: {pop_2020:,} - {pop_2010:,} = {growth:,}")