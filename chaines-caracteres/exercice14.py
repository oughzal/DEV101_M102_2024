# Exercice 14
def startWith(s:str) -> list[str]:
    # return list(filter(lambda w : w.startswith("a"),s.split()))
    L = s.split()
    result = []
    for w in L:
        if w.startswith("a"):
            result.append(w)
    return result
    
print(startWith("abc ef af xy az"))

