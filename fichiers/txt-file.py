
# lire le fichier file1.txt
file = open("fichiers/file1.txt","r")
#  traitements
print(file.read())
file.close()
# Ecrire dans le fichier file2.txt
file = open("fichiers/file2.txt","a")
file.write("\nBonjour tout le monde")
file.close()

# lire file1 ligne par ligne
file = open("fichiers/file1.txt","r")
for line in file:
    print(line.strip())
file.close()
# lire les ligne dans une liste
file = open("fichiers/file1.txt","r")
lines = file.readlines()
print(lines)
file.close
#Ecrire une liste dans un fichier
lines = ["Bonjour\n","Tout le monde\n","Comment allez-vous\n","Je suis content de vous voir\n"]
file = open("fichiers/file3.txt","w")
file.writelines(lines)
file.close()

#utiliser le bloc with
with open("fichiers/file1.txt","r") as file:
    print(file.read())

import os

if os.exists("fichiers/file10.txt"):
    file = open("fichiers/file10.txt","r")

if os.exists("fichiers/file10.txt"):
    os.remove("fichiers/file10.txt")


