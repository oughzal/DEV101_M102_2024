# 1. Créez un fichier texte appelé exemple.txt contenant plusieurs lignes de texte.
# 2. Écrivez un programme qui ouvre ce fichier en mode lecture et affiche chaque ligne séparément.
with open('fichiers/exemple.txt', 'r') as file:
    for line in file:
        print(line.strip())
file = open("fichiers/exemple.txt","r")
for line in file:
    print(line.strip())
file.close()
# 3. Assurez-vous que le fichier est fermé correctement après la lecture.


    