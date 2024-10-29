import os
notes =[]
if os.path.exists("fichiers/notes.txt"):
    file = open("fichiers/notes.txt","r")
    for line in file:
        notes.append(float(line.strip()))
    file.close()
print(notes)
    