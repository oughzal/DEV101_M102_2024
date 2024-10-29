import csv

with open('fichiers/commandes.csv', 'w') as file:
    header = ['nom', 'produit', 'quantite']
    writer = csv.DictWriter(file, fieldnames=header)
    writer.writeheader()
    writer.writerow({'nom': 'Jean', 'produit': 'Pain', 'quantite': 2})
    writer.writerow({'nom': 'Paul', 'produit': 'Lait', 'quantite': 3})
    writer.writerow({'nom': 'Pierre', 'produit': 'Eau', 'quantite': 5})
