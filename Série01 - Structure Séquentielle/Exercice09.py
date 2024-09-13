from math import sqrt
# //Entrée
Xa = float(input("Xa : "))
Ya = float(input("Xa : "))
Xb = float(input("Xa : "))
Yb = float(input("Xa : "))
# //Traitement
D = sqrt((Xa-Xb)**2 + (Ya-Yb)**2)
D = ((Xa-Xb)**2 + (Ya-Yb)**2)**0.5
# //Sortie
print("La distance est ", D)