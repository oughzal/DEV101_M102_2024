import csv
étudiants = []
with open('fichiers/etudiants.csv', 'r') as file:
    reader = csv.DictReader(file,delimiter=";")
    for row in reader:
        row["note"] = 20
        étudiants.append(row)

with open('fichiers/etudiants.csv', 'w') as file:
    fieldnames = ["nom","prenom","note"]
    writer = csv.DictWriter(file, fieldnames=fieldnames,delimiter=";")
    writer.writeheader()
    for etudiant in étudiants:
        writer.writerow(etudiant)
# comment ne pas lisser une ligne vide avec writer
# with open('fichiers/etudiants.csv', 'w') as file:
#     fieldnames = ["nom","prenom","note"]
#     writer = csv.DictWriter(file, fieldnames=fieldnames,delimiter=";")
#     writer.writeheader()
#     for etudiant in étudiants:
#         if etudiant["nom"] != "":
#             writer.writerow(etudiant)
