#exercice 5
def estPremier(N:int)-> bool :
    if N==1 or N==2 :
        return True
    for i in range (2,N):
        if N % i == 0 :
            return False
    return True
print(estPremier(5))
print(estPremier(6))
print(estPremier(23))