T=[0,1,2,3,4,5,6,7,8,9]

v = int(input("donner la valeur de v : "))
i=0
while i< len(T) and T[i]!=v :
    i=i+1

if i >=len(T) :
    print("la position de ", v, " est -1")
else:
    print("la position de ", v, " est ",i)
p = T.index(v) if v in T else -1
print(f"La position de {v} est {p}")