# //Entrée
H= int(input("H : "))
M= int(input("M : "))
S= int(input("S : "))
D= int(input("D : "))
# print(H,":",M,":",S," + ", D , " sec = ",sep="",end="")
print(f"{H}:{M}:{S} + {D} sec = ",end="")

# //Traitement
S = S + D
M = M + S // 60
S = S % 60
H = H + M //60
M = M % 60
H = H % 24 
# //Sortie
# print(H,":",M,":",S,sep="")
print(f"{H}:{M}:{S}")