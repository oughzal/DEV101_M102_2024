# Exercice 11.5
def wordSort(s:str)->str:
    return " ".join(sorted(s.split(),key=lambda w : w.lower()))

print(wordSort("xy e DEV Python PHP Koltin adroid"))