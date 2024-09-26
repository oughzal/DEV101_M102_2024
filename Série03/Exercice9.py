N = int(input("donner n :")) 
S = 0
while N != 0 :
    S = S + N % 10
    N = N // 10
print("La somme est ", S)