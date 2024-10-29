import csv


persons =[
    ["Nom", "Prénom", "Département"],
    ["Leblanc", "Sophie", "RH"],
    ["Marchand", "Pierre", "Finance"]
    ]
with open('fichiers/emplyee.csv', 'w') as f:
    reader = csv.writer(f)
    for person in persons:
        reader.writerow(person)

with open('fichiers/emplyee.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)