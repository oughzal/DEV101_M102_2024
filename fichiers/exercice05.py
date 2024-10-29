import csv
with open('fichiers/etudiants.csv', 'r') as file:
    reader = csv.DictReader(file,delimiter=";")
    for row in reader:
        print(row)