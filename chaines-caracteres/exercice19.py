# Exercice 19
def nbMinMaj(s :str)->tuple:
    nbMin =0
    nbMaj = 0
    for c in s:
        if 'a'<= c <= 'z':
            nbMin += 1
        if 'A'<= c <= 'Z':
            nbMaj += 1
    return (nbMin,nbMaj)

print(nbMinMaj("DeV PYtHoN"))
        
