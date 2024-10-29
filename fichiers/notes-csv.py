import csv
# lire le fichier notes.csv
with open('fichiers/notes.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Ecrire dans le fichier notes.csv
notes = [["note1","note2","note3"],[12, 15, 20], [13, 14, 19], [14, 16, 18]]
with open('fichiers/notes2.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(notes)

#lire csv sous forme de dictionnaire
with open('fichiers/notes.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

#Ecrire dans le fichier notes.csv sous forme de dictionnaire
notes = [{"note1":12,"note2":15,"note3":20},{"note1":13,"note2":14,"note3":19},{"note1":14,"note2":16,"note3":18}]
with open('fichiers/notes3.csv', 'w') as file:
    fieldnames = ["note1","note2","note3"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for note in notes:
        writer.writerow(note)

