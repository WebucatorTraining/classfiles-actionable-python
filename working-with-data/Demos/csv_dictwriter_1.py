import csv

grades = [
    {
        "English": 97,
        "Math": 93,
        "Art": 74,
        "Music": 86
    },
    {
        "English": 89,
        "Math": 83,
        "Art": 97,
        "Music": 94
    }
]

csv_file = '../data/grades.csv'
with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Math', 'Art', 'English', 'Music']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(grades)