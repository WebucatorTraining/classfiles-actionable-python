import csv

grades = [
    {
        "English": 88,
        "Math": 88,
        "Art": 88,
        "Music": 88
    },
    {
        "English": 77,
        "Math": 77,
        "Art": 77,
        "Music": 77
    }
]

csv_file = '../data/grades.csv'
with open(csv_file, 'a', newline='', encoding='utf-8') as csvfile:
    fieldnames = grades[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writerows(grades)