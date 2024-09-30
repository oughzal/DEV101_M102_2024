T =[4,3,-3,-7,7,8,-9,-5,6,-4]
Sp=0
Sn=0
for e in T:
    if e<0 :
         Sn = e + Sn
    else:
        Sp = e + Sp
print("la somme des valeurs positifs:",Sp)
print("la somme des valeurs négatifs:",Sn) 