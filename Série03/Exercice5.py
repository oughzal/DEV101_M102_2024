N = int(input("Entrer N : "))

#Méthode 1
S = 0
if N % 2 == 0 :
    for i in range(0,N+1,2):
        S = S + i  
else :  
    for i in range(1,N+1,2):
        S = S + i 
print("la somme S = ",S) 
#Méthode 2
S = 0
for i in range(1,N+1):
    if N % 2 == 0 and i % 2 == 0:
        S = S+i
    if N % 2 != 0 and i % 2 != 0:
        S = S+i

print("La somme S = ",S)
#Méthode 3
S= 0
for i in range (N,0,-2):
    S= S+i
print("la somme est :", S)
