import json
# lire le fichier file.json
with open('fichiers/file.json') as f:
    data = json.load(f)
    for row in data:
        print(row)
# Ecrire dans le fichier file.json
data = [{"nom":"Jean","age":25},{"nom":"Pierre","age":30},{"nom":"Paul","age":28}]
with open('fichiers/file2.json', 'w') as f:
    json.dump(data, f)