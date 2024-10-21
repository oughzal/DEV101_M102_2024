# Créer une liste vide
L = []
L = list()
# Créer et initialiser une liste
L = [17,5,7,8,11,3,6]
#afficher la liste
print(f"L={L}")
#accès aux éléments de la liste
print(L[0])
L[1] = 7
#Ajouter un élément à la fin de la liste
L.append(4)
#insérer un élément à une position spécifique
L.insert(0,9)

# Copier une liste
L2 = L.copy()
L2 = L[:]
# Affectation de liste
L1 = L # L1 est L (la modification des éléments d'un affecte l'autre)

