import datetime

def str_to_date(str_date):
    date_parts = [int(i) for i in str_date.split("-")]
    return datetime.date(*date_parts)

str_date = input('Input date as YYYY-MM-DD: ')
date = str_to_date(str_date)
print(date)