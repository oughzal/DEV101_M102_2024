import json
with open('fichiers/donnees.json') as f:
    data = json.load(f)
    print(data)

data['ville'] = 'Paris'
with open('fichiers/donnees.json', 'w') as f:
        json.dump(data, f)