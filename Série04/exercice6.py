T = [12,13,10,6,20,16,11,9,7,15]
M=0
for e in T:
    M=M+e
M=M/len(T)
M = sum(T)/len(T)
print("Moyenne = ",M) 
for e in T:
    if e >= M :
        print(e,end=";")
print()
print(f"{list(filter(lambda e : e>=M,T))}")
