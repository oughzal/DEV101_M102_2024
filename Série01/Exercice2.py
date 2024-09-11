# Entrée
PU = float(input("Donner PU : "))
Qt = int(input("Donner Qt : "))
# Traintement
TVA = 0.2
HT = PU*Qt
TTC = HT + HT*TVA
#Sortie
print("TTC =", TTC)