# Écrivez un programme qui lit ce fichier CSV et affiche chaque ligne sous forme de liste.
import csv
with open('fichiers/etudiants.csv', 'r') as file:
    reader = csv.reader(file,delimiter=";")
    for row in reader:
        print(row)