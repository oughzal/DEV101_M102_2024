# 1. Créez un programme qui ouvre un fichier texte appelé sortie.txt en mode écriture.
file = open("fichiers/sortie.txt","w")
# 2. Écrivez plusieurs lignes dans ce fichier en utilisant write().
file.write("Bonjour\n")
file.write("Tout le monde\n")
file.write("Comment allez-vous\n")
file.write("Je suis content de vous voir\n")
file.close()
# 3. Ouvrez à nouveau le fichier en mode ajout et ajoutez une nouvelle ligne.
file = open("fichiers/sortie.txt","a")
file.write("Je suis content de vous voir\n")
file.close()
# 4. Lisez le fichier pour vérifier que le contenu a été correctement ajouté.
with open("fichiers/sortie.txt","r") as file:
    print(file.read())
    