T = [1,2,3,4,5,6,7,8]
i = 0
j = len(T) -1
while i <j:
    T[i],T[j] = T[j],T[i]
    i += 1
    j -= 1
print(T)

T = [1,2,3,4,5,6,7,8]
T.reverse()
print(T)

T = [1,2,3,4,5,6,7,8]
T1 = list(reversed(T))
print(f"T ={T} ; T1 ={T1}")

T = [3,5,1,4,2]
T.sort()
print(T)
T = [3,5,1,4,2]
T1 = list(sorted(T))
print(f"T ={T} ; T1 ={T1}")

T = ["3","5","1","14","2"]
T.sort(reverse=True,key= lambda s : int(s))
print(T)