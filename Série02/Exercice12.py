# Algorithme Exercice12
# Var
# J,M,A : Entier
# Début
# Ecrire("Donner le jour : ")
# Lire(J)
J=int(input("donner le jour : "))
# Ecrire("Donner le mois : ")
# Lire(M)
M=int(input("donner le mois : "))
# Ecrire("Donner l'année : ")
# Lire(A)
A=int(input("donner l'annes : "))
                
if M<1 or M>12 :
# Ecrire("Date invalide") 
    print("date invalide")
# SinonSi J<1 ou J>31 Alors
elif J<1 or J>31 :
    print("Date invalide")      
elif J==31 and (M==2 or M==4 or M==6 or M==9 or M==11) :
    print("Date invalide") 
elif J==30 and M==2 :
    print("Date invalide") 
elif J==29 and M==2 and not (A%400==0 or (A%4==0 and A%100!=0)) :
    print("Date invalide") 
else :
    print("Date valide")


# Ecrireln()

# Si J>=1 et J<=28 et M>0 et M<=12 Alors
# Ecrire("Date valide")
# SinonSi J=31 et (M=1 ou M=3 ou M=5 ou M=7 ou M=8 ou M=10 ou M=12) Alors
# Ecrire("Date valide")
# SinonSi J=30 et M!=2 et M>=1 et M<=12 Alors
# Ecrire("Date valide")
# SinonSi J=29 et M!=2 et M>=1 et M<=12 Alors
# Ecrire("Date valide")
# SinonSi J=29 et M=2 et (A%400=0 ou (A%4=0 et A%100!=0)) Alors
# Ecrire("Date valide")
# Sinon
# Ecrire("Date invalide")
# FinSi
# Fin
