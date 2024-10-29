#lire un fichier binaire
with open('fichiers/image.jpg', 'rb') as file:
    data = file.read()
    print(data)
#ecrire dans un fichier binaire
with open('fichiers/image2.jpg', 'wb') as file:
    file.write(data)