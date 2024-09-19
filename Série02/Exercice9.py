note=float(input("Donner la note : "))
if note >=16 and note<=20:
    print("Très-bien")
elif note >=14:
    print("bien")
elif note >=12:
    print("Assez-bien")
elif note >=10:
    print("Passable")
elif note >=0:
    print("Redoublant")
else:
    print("Erreur")