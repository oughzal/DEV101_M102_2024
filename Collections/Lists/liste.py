#Liste
L = [1,2,3,4]
print(L[1])
print(L[-1])
# Méthodes

#ajouter à la fin
L.append(5)
#insérer 
L.insert(0,6)
print(L)

#supprimer
L.remove(2) # valeur
v = L.pop() # par indice -1
L.pop(2) # indice 2

del L[1]
del L[:]
L.clear() # tout les élément
# trier (sort)
L = [2,1,0,5,3,7]
L2 = sorted(L)
print(L2)
L.sort()
print(L)
L.sort(reverse=True)
print(L)

#inverser la liste
L.reverse()
L3 = reversed(L)

L = [1,2,3]
L2 = [4,5,6]
L.extend(L2)
L.extend([7,8])
L = L + [9,10,11,6,6,6,6]

print(L.count(6))

print(L.index(10) if 10 in L else -1)

# Fonction
print(len(L)) # nombre d'élément

L4 = list(range(1,11))
print(L4)
print(list("DEV101"))

# opérateurs
L = [1,2,3] + [4,5,6]
print(L)
print([1,2]*3)

#TP
notes = [11,13,17,16,20,18]
notes.append(12)
notes.insert(0,19)
notes[1] = 18
print(notes)

#créer liste vide
L = []
L = list()

# Tuple
T = (1,2,3,4)
print(T[1])
print(T)


