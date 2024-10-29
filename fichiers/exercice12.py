texte = ""
with open("fichiers/fichier1.txt", "r") as f: # read
    texte = f.read()

with open("fichiers/fichier_combine.txt", "w") as f: # write
    f.write(texte)

with open("fichiers/fichier2.txt", "r") as f: # read
    texte = f.read()

with open("fichiers/fichier_combine.txt", "a") as f: # append
    f.write("\n"+texte)
