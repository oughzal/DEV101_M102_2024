# Exercice 9
def estBissextile(A : int) -> bool:
    return  A % 400 == 0 or (A % 4 == 0 and A % 100 != 0)

def dateValide(j : int, m: int, a : int) -> bool :
    if j<1 or j> 31 or m<1 or m>12  :
        return False
    elif j==31 and (m==2 or m==4 or m==6 or m==9 or m== 11)  :
        return False 
    elif  j==30 and m==2 :
            return False
    elif j==29 and m==2 and not estBissextile(a) :
        return False
    else :
        return True
print(dateValide(4,10,2024)) 
print(dateValide(31,6,2024))
print(dateValide(29,2,2024))
print(dateValide(29,2,2025))
   