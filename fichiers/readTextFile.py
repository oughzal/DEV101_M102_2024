# lire tous le contenu
file = open("file1.txt","r") # ouvrir le fichier
content = file.read()
# print(content)
file.close() #fermer le fichier

#lire un certain nombre des caractères
file = open("file1.txt","r")
file.seek(24)
content = file.read(6)
print(content)
file.close()

# Lire les lignes du fichier
with open("file1.txt") as file:
    lines = file.readlines()
    # print(lines)

# Lire ligne par ligne
with open("file1.txt") as file :
    line = file.readline()
    while line != "":
        # print(line.strip())
        line = file.readline()

