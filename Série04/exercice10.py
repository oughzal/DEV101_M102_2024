T = [1,2,3,1,4,5,2,6,7,9]

for i in range(len(T)) :
    c = 0
    for j in range(len(T)) :
        if T[i] == T[j] and i != j : 
            c += 1
            break
    if c == 0 :
        print(T[i], end= ", ")
print()

for e in T :
    if T.count(e)==1:
        print(e, end= ", ")



