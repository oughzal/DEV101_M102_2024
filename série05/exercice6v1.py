#Exercice6 v1
def estPremier(N:int)-> bool :
    if N==1 or N==2 :
        return True
    for i in range (2,N):
        if N % i == 0 :
            return False
    return True

def listPremiers(N:int) ->list :
    L = []
    for i in range(1,N+1):
        if estPremier(i):
            L.append(i)
    return L
L = listPremiers(100000)
print(L)
print(len(L))