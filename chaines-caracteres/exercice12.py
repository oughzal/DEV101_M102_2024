# Exercice 12
def nbVoyelles(s:str)->int:
    v = "oieauy"
    # nb = 0
    # for c in s:
    #     if c in v:
    #         nb += 1
    # return nb
    return len(list(filter(lambda e : e in "oieauy", s)))
print(nbVoyelles("abcdeyzi"))