import csv

with open('csvname.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimeter=',')
    rows = list(csvreader)
    for row in rows[:2]:
        print(', '.join(row))


with open('csvname.csv', newline='') as csvfile:
    csvreader = csv.DictReader(csvfile, delimeter=',')
    rows = list(csvreader)
    for row in rows[:2]:
        print(', '.join(row))
