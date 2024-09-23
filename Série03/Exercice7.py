N = int(input("Donner un nombre : "))
for i in range(2,N):
    if i==3:
        continue # passer à l'itération suivante
    if N % i == 0:
        break # arrête la boucle
if i==N:
    print(f"{N} est premier")
else:
    print(f"{N} n'est pas premier")