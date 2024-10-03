#Exercice 6 v2
def listPremiers(N):
    L=[]
    for i in range(2,N+1):
        p = True
        for e in L:
            if i % e==0:
                p =False
                break
        if p == True :
            L.append(i)
    L.insert(0,1)
    return L

L = listPremiers(100000)
print(L)
print(len(L))