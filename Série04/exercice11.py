T1 = [1,2,3,4]
T2 = [5,6,7,8,9]

T3 =[]
for e in T1 : 
    T3.append(e)
for e in T2 : 
    T3.append(e)

print(T3)

T3 = T1 + T2
T4 = T1*5
print(T4)
print("Hello "*10)