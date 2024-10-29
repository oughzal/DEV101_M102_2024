# Lire un fichier binaire (par exemple, une image)
with open("image.png", "rb") as fichier_binaire:
    contenu_binaire = fichier_binaire.read()
    print(contenu_binaire)

# Écrire dans un fichier binaire
with open("nouvelle_image.png", "wb") as fichier_binaire:
    fichier_binaire.write(contenu_binaire)
