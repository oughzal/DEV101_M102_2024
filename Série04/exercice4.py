T = [11,15,10,18,20,6]
m = T[0]
for e in T:
    if e > m :
        m = e
print(f"Le max est {m}")
print(f"Le max est {max(T)}")
print(f"Le min est {min(T)}")
print(f"Le somme est {sum(T)}")