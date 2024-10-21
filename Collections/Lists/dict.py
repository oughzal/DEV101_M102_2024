#Map hashmap
d ={
    "nom" : "Bnu",
    "prenom" : "mohammed",
    "age" : 20,
    "groupe" : "DEV101"
    }
print(d["prenom"])
print(d.get("genre","M"))

keys = list(d.keys())
print(keys)

values = list(d.values()) 
print(values)

items = list(d.items())
print(items)

for k in d:
    print(f"{k} : {d[k]}")
for v in d.values():
    print(v)
for k,v in d.items():
    print(f"{k} : {v}")

d.pop("groupe")
print(d)

#TP
notes = {
    "etudiant1" : 12,
    "etudiant2" : 18,
    "etudiant3" : 10,
    "etudiant4" : 16,
    "etudiant5" : 15,
}
notes["etudiant6"] = 17 # Ajouter/
notes.pop("etudiant1")
del notes["etudiant2"]