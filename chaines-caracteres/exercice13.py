# Exercice 13
def nthWord(s:str,n:int)->str:
    L = s.split()
    print(L)
    print(len(L))
    return L[n-1] if len(L) > n else None

print(nthWord("DEV 101 M102 Algo Python",3))
