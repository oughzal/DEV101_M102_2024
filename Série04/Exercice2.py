N = int(input("Donner le nombre des élément du tableau :"))
T =[]
for i in range(N):
    v = int(input(f"Donner T[{i}] : "))
    T.append(v)
print(f"T = {T}")
print(f"nombre des élément est {len(T)}")