# 1. Créez un programme qui crée un fichier CSV appelé produits.csv.
# 2. Écrivez les informations suivantes sous forme de dictionnaires :
# Produit, Prix, Quantité
# Ordinateur, 1500, 10
# Clavier, 50, 100
# Souris, 25, 200
import csv


with open('fichiers/produits.csv', 'w') as file:
    fieldnames = ["Produit", "Prix", "Quantité"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"Produit":"Ordinateur","Prix":1500,"Quantité":10})
    writer.writerow({"Produit":"Clavier","Prix":50,"Quantité":100})
    writer.writerow({"Produit":"Souris","Prix":25,"Quantité":200})
# 3. Vérifiez que les données sont correctement formatées
with open('fichiers/produits.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)