S = set()
S.add(1)
S.add(2)
S.add(7)
S.add(1)
S.add(3)
S.add(1)
print(S)

L = [1,2,3,1,4,2,7,6,4,4,3,8]
L = list(set(L))
S = set(L)
L = list(S)
print(L)

S1 = set([1,2,3,4,5])
S2 = set([1,2,3,8,9,10])
print(S1.union(S2))
print(S2.union(S1))
print(S2.intersection(S1))
print(S1.difference(S2))
print(S2.difference(S1))
