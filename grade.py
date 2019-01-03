import csv

with open('gpa.csv') as csvfile:
    read_csv = csv.reader(csvfile, delimiter = ',')
    for row in read_csv:
        print(row)
