N = int(input("donner le nombre des elements: "))
T = []
for i in range(N):
    V=int(input(f"Donner l element {i}:"))
    T.append(V)
S,P=0,1
#Méthode 1
for i in range(len(T)):
    S+=T[i]
    P*=T[i]
S,P=0,1
#Méthode 2
for e in T:
    S+= e
    P*=e
M = S / len(T)

print("La somme = ",S)
print("La Produit = ",P)
print("La moyenne = ",M)