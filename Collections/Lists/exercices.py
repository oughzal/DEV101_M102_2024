# Partie 1 : Manipulation des Listes

# 1. Créez une liste notes contenant les notes suivantes : 15, 18, 12, 20, 14.
notes=[15,18,12,20,14]
# 2. Ajoutez une nouvelle note (17) à la fin de la liste.
notes.append(17)
# 3. Insérez une note de 10 au début de la liste.
notes.insert(0,10)
# 4. Remplacez la note située à l'indice 3 par 19.
notes[3]=19
# 5. Supprimez la première occurrence de la note 12.
notes.remove(20)
# 6. Supprimez et affichez la dernière note de la liste.
notes.pop()

# 7. Triez la liste dans l'ordre croissant puis inversez l'ordre.
notes.sort()
notes.sort(reverse=True)
# 8. Affichez les trois premières notes triées en utilisant le slicing.
print(sorted(notes[0:3]))


# 9. Calculez et affichez la somme totale des notes.
print(sum(notes))
# 10. Créez une nouvelle liste en concaténant deux copies de la liste notes.
copie1 = notes*2
copie2 = notes + notes
copie = notes.copy() + notes[:]
# 11. Répétez trois fois la liste notes pour créer une nouvelle liste.
L=notes*3
L=notes+notes+notes
# Partie 2 : Manipulation des Tuples

# 1. Convertissez la liste notes triée en tuple.
T=tuple(notes)
# 2. Accédez et affichez la note située à l'indice 2 du tuple.
print(T[2])
# 3. Essayez de modifier une valeur du tuple (constatez que cela n’est pas possible).
# T[2] =4
# 4. Trouvez l'indice de la première occurrence de la note 19 dans le tuple.
print(T.index(19))
# 5. Calculez la somme des éléments du tuple et affichez la note minimale et maximale.
print(sum(T))
# Partie 3 : Manipulation des Dictionnair
# 1. Créez un dictionnaire etudiants_notes où les clés sont les noms d'étudiants (ex. "Alice", "Bob", "Charlie") et les valeurs sont leurs notes (utilisez les notes de la liste notes).
etudiants= {
    'E1' : 12,
    'E2' : 16,
    'E3' : 20,
    'E4' : 17,
    'E5' : 19,
    'E6' : 9,
    }
# 2. Ajoutez un nouvel étudiant "David" avec la note 18.
etudiants["E7"] = 18
# 3. Modifiez la note de "Charlie" en la passant à 20.
etudiants['E5'] = 20
# 4. Supprimez l'étudiant "Bob" du dictionnaire et affichez sa note supprimée.
print(etudiants.pop("E3"))
# 5. Parcourez le dictionnaire et affichez les noms et les notes de chaque étudiant.
for k,v in etudiants.items() : 
  print(k,":",v) 
# 6. Affichez toutes les clés (noms d'étudiants) du dictionnaire.
keys= etudiants.keys()
print(keys)
# 7. Affichez toutes les valeurs (notes des étudiants) du dictionnaire.
for v in etudiants.values() :
  print(v)
# 8. Utilisez la méthode get() pour tenter d'accéder à la note de "Eve", en fournissant une valeur par défaut "Non noté".
print(etudiants.get("eve","Non noté"))
# 9. Videz complètement le dictionnaire à la fin de l’exercice.
etudiants.clear()
# Partie 4 : Manipulation des Ensembles

# 1. Créez un ensemble cours_1 contenant les étudiants inscrits au premier cours : "Alice", "Bob", "Charlie".
cours_1=set(["Alice" , "Bob" , "Charlie"])
# 2. Créez un ensemble cours_2 contenant les étudiants inscrits au deuxième cours : "Charlie", "David", "Eve".
cours_2 = set(["Charlie","David","Eve"])
# 3. Ajoutez un nouvel étudiant "Frank" à l'ensemble cours_1.RS81
cours_1.add("Frank")
# 4. Supprimez "Bob" de l'ensemble cours_1 en utilisant remove().
cours_1.remove("Bob")
# 5. Vérifiez si "Eve" est inscrite dans cours_1 en utilisant l'opérateur in.
print("Eve" in cours_1)
# 6. Trouvez l'union des ensembles cours_1 et cours_2 (étudiants inscrits à au moins un des deux cours).
# 7. Trouvez l'intersection des ensembles cours_1 et cours_2 (étudiants inscrits aux deux cours).
# 8. Affichez la différence entre cours_1 et cours_2 (étudiants inscrits uniquement à cours_1).
# Partie 5 : Exercice Final
# 1. Créez une liste contenant les notes de 8 étudiants.
# 2. Ajoutez deux nouvelles notes à la fin de la liste.
# 3. Convertissez la liste en tuple pour en garantir l’immuabilité.
# 4. Créez un dictionnaire associant chaque étudiant à sa note.
# 5. Créez deux ensembles d'étudiants, l'un pour ceux ayant une note supérieure à 15 et l'autre pour ceux ayant une note supérieure à 18.
# 6. Affichez l’union et l’intersection de ces deux ensembles.
