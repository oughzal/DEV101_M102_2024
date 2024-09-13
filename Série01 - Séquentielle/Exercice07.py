# //Entrée
# Ecrire("Donner la durée en secondes : ")
# Lire(T)
T =int(input("donner la durée en secondes : "))
# //Traitement
H = T // 3600
T = T % 3600 # Le reste (M+S)
M = T // 60
S = T % 60
# //Sortie
print(H,":",M,":",S,sep="")
print(f"{H}:{M}:{S}") # F-String