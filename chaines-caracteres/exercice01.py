# Exercice 1
def nbOccurence(ch:str,e:str)->int :
    return ch.count(e)
    nb = 0
    for c in ch:
        if c==e:
            nb +=1
    return nb
print(nbOccurence("abcaefada","a"))