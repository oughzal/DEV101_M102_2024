#Écrire dans un fichier
with open("file2.txt","w") as file:
    for i in range(1,11):
        file.write(f"line number {i}\n")
    lines = ["ligne 12\n","ligne 13\n","ligne 14\n",]
    file.writelines(lines)

# Ajouter à la fin du fichier
with open("file2.txt","a") as file:
    file.write("ligne 15\n")
    

# Lire/écrire dans un fichier
